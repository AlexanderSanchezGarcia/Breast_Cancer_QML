# fuente: Code/3_Feature_Extraction.ipynb · celda de código 3 · líneas 1-13
extractor = featureextractor.RadiomicsFeatureExtractor(binCount=32, force2D=True, label=1)
extractor.disableAllFeatures()
for fam in FAMILIES:
    extractor.enableFeatureClassByName(fam)

print("Settings:")
for k in ("binCount", "force2D", "distances", "normalize", "resampledPixelSpacing", "label"):
    print(f"  {k:22s}: {extractor.settings.get(k)}")
print(f"Image types: {list(extractor.enabledImagetypes)}")

probe = index.iloc[0]
probe_feats = extractor.execute(str(DATA_DIR / probe.path_image), str(DATA_DIR / probe.path_mask))
FEATURES = [k for k in probe_feats if k.startswith("original_")]
