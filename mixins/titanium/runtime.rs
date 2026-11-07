//! TITANIUM's testable skin metadata and PNG validation core.
//! Game UI, filesystem import, and player-render integration are separate milestones.

#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub enum ArmModel {
    Classic,
    Slim,
}

#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub struct SkinInfo {
    pub width: u32,
    pub height: u32,
    pub model: ArmModel,
}

/// Validate the PNG signature and the dimensions in its first IHDR chunk.
/// Supports standard 64x64 skins and legacy 64x32 skins.
pub fn inspect_skin_png(bytes: &[u8], model: ArmModel) -> Result<SkinInfo, &'static str> {
    const SIGNATURE: &[u8; 8] = b"\x89PNG\r\n\x1a\n";
    if bytes.len() < 24 || &bytes[..8] != SIGNATURE {
        return Err("not a valid PNG header");
    }
    if &bytes[12..16] != b"IHDR" {
        return Err("PNG is missing its IHDR header");
    }
    let width = u32::from_be_bytes([bytes[16], bytes[17], bytes[18], bytes[19]]);
    let height = u32::from_be_bytes([bytes[20], bytes[21], bytes[22], bytes[23]]);
    if width != 64 || (height != 64 && height != 32) {
        return Err("skin PNG must be 64x64 or legacy 64x32");
    }
    Ok(SkinInfo { width, height, model })
}

#[cfg(test)]
mod tests {
    use super::*;

    fn png_header(width: u32, height: u32) -> [u8; 24] {
        let mut bytes = [0u8; 24];
        bytes[..8].copy_from_slice(b"\x89PNG\r\n\x1a\n");
        bytes[12..16].copy_from_slice(b"IHDR");
        bytes[16..20].copy_from_slice(&width.to_be_bytes());
        bytes[20..24].copy_from_slice(&height.to_be_bytes());
        bytes
    }

    #[test]
    fn accepts_classic_and_slim_skin_dimensions() {
        let bytes = png_header(64, 64);
        assert_eq!(inspect_skin_png(&bytes, ArmModel::Classic).unwrap().model, ArmModel::Classic);
        assert_eq!(inspect_skin_png(&bytes, ArmModel::Slim).unwrap().model, ArmModel::Slim);
    }

    #[test]
    fn accepts_legacy_skin_dimensions() {
        assert_eq!(inspect_skin_png(&png_header(64, 32), ArmModel::Classic).unwrap().height, 32);
    }

    #[test]
    fn rejects_wrong_dimensions_and_non_png() {
        assert!(inspect_skin_png(&png_header(128, 128), ArmModel::Classic).is_err());
        assert!(inspect_skin_png(b"not a png file", ArmModel::Slim).is_err());
    }
}
