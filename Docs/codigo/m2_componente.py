# fuente: Code/2_Preprocessing.ipynb · celda de código 11 · líneas 1-13
def prepare_mask(i):
    # Aligned, cleaned mask (uint8, 0/1) in the image space, plus cleaning diagnostics
    row = df.loc[i]
    raw = (pydicom.dcmread(row.path_roi_mask).pixel_array > 0).astype(np.uint8)
    m = align_mask(raw, (row.img_rows, row.img_cols), row.mismatch)
    n, lab, st, _ = cv2.connectedComponentsWithStats(m, connectivity=8)
    if n <= 2:
        return m, 0, 0.0
    k = 1 + int(np.argmax(st[1:, cv2.CC_STAT_AREA]))
    main = (lab == k).astype(np.uint8)
    rest = (lab > 0) & (lab != k)
    reach = cv2.distanceTransform(1 - main, cv2.DIST_L2, 5)[rest].max()
    return main, int(rest.sum()), float(reach)
