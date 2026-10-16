# fuente: Code/2_Preprocessing.ipynb · celda de código 13 · líneas 7-26
def export_mammogram(item):
    path_full, idxs = item
    img = pydicom.dcmread(path_full).pixel_array
    eq = cv2.createCLAHE(clipLimit=CLAHE_CLIP, tileGridSize=CLAHE_TILES).apply(to_uint8(img))
    recs = []
    for i in idxs:
        row = df.loc[i]
        mask, _, _ = prepare_mask(i)
        y0, y1, x0, x1 = bbox(mask)
        Y0, Y1 = max(0, y0 - MARGIN), min(img.shape[0], y1 + MARGIN)
        X0, X1 = max(0, x0 - MARGIN), min(img.shape[1], x1 + MARGIN)
        base = OUT_DIR / row.finding_type / row.case_id
        paths = {k: base.with_name(f"{row.case_id}_{k}.nrrd") for k in ("image", "mask", "clahe")}
        write_nrrd(img[Y0:Y1, X0:X1], paths["image"])
        write_nrrd(mask[Y0:Y1, X0:X1], paths["mask"])
        write_nrrd(eq[Y0:Y1, X0:X1], paths["clahe"])
        recs.append(dict(i=i, crop_y0=Y0, crop_x0=X0, crop_h=Y1 - Y0, crop_w=X1 - X0,
                         margin_clipped=(Y0 > y0 - MARGIN) or (Y1 < y1 + MARGIN) or (X0 > x0 - MARGIN) or (X1 < x1 + MARGIN),
                         **{f"path_{k}": str(p.relative_to(DATA_DIR)) for k, p in paths.items()}))
    return recs
