# fuente: Code/2_Preprocessing.ipynb · celda de código 5 · líneas 1-10
def align_mask(mask, shape, kind):
    H, W = shape
    if kind == "none":
        return mask
    if kind == "scaled":
        return cv2.resize(mask, (W, H), interpolation=cv2.INTER_NEAREST_EXACT)
    out = np.zeros((H, W), mask.dtype)          # "offset": same scale, top-left anchor
    h, w = min(H, mask.shape[0]), min(W, mask.shape[1])
    out[:h, :w] = mask[:h, :w]
    return out
