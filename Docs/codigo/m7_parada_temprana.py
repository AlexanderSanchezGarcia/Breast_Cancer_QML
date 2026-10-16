# fuente: Code/7_Classification.ipynb · celda de código 3 · líneas 44-68
    best, best_state, best_epoch, wait = np.inf, None, 0, 0
    for epoch in range(1, (fixed or MAX_EPOCHS) + 1):
        model.train()
        order = torch.randperm(len(xt), generator=gen)
        for i in range(0, len(xt), BATCH):
            b = order[i:i + BATCH]
            opt.zero_grad()
            (loss_fn(model(xt[b]), yt[b]) * wt[b]).mean().backward()
            opt.step()
        if fixed:
            continue
        model.eval()
        with torch.no_grad():
            val = float((loss_fn(model(xv), yv) * wv).mean())
        if val < best - 1e-6:
            best, best_state, best_epoch, wait = val, copy.deepcopy(model.state_dict()), epoch, 0
        else:
            wait += 1
            if wait >= PATIENCE:
                break
    if not fixed:
        model.load_state_dict(best_state)
    model.eval()
    with torch.no_grad():
        return torch.sigmoid(model(prep(x_eval))).numpy(), (fixed or best_epoch)
