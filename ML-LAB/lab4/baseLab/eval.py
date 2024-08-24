import mat73
import numpy as np

import config


def my_nn(x, q, k):
    sim = q @ x.T
    dis = np.sort(sim, axis=1)[:, ::-1]
    idx = np.argsort(sim, axis=1)[:, ::-1]
    dis = dis[:, :k].T
    idx = idx[:, :k].T

    idx += 1
    return idx, dis


def compute_map(ranks, gnd):
    map = 0
    nq = 500
    aps = np.zeros((nq, 1))
    for i in range(nq):
        qgnd = gnd['ok'][i][0].reshape(-1)
        qgndj = gnd['junk'][i][0].reshape(-1)
        # positions of positive and junk images
        _, pos, _ = intersect_mtlb(ranks[:, i], qgnd) + np.array([1])
        # _, junk, _ = intersect_mtlb(ranks[:, i], qgndj)
        junk = np.array([1])
        pos = np.sort(pos)
        # junk = np.sort(junk)
        k = 0
        ij = 1
        if len(junk):
            # decrease positions of positives based on the number of junk images appearing before them
            ip = 1
            while ip <= np.size(pos):
                while (ij <= len(junk) and pos[ip - 1] > junk[ij - 1]):
                    k += 1
                    ij += 1
                pos[ip - 1] -= k
                ip += 1
        ap = score_ap_from_ranks1(pos, len(qgnd))
        map += ap
        aps[i] = ap
    map /= nq
    return map, aps


def intersect_mtlb(a, b):
    # Realize MATLAB's intersect(a, b)
    a1, ia = np.unique(a, return_index=True)
    b1, ib = np.unique(b, return_index=True)
    aux = np.concatenate((a1, b1))
    aux.sort()
    c = aux[:-1][aux[1:] == aux[:-1]]
    return c, ia[np.isin(a1, c)], ib[np.isin(b1, c)]


def score_ap_from_ranks1(ranks, nres):
    # This function computes the AP for a query
    nimgranks = len(ranks)  # number of images ranked by the system
    ranks -= np.array([1])
    # accumulate trapezoids in PR-plot
    ap = 0
    recall_step = 1 / nres
    for j in range(nimgranks):
        rank = ranks[j]
        if rank == 0:
            precision_0 = 1.0
        else:
            precision_0 = j / rank

        precision_1 = (j + 1) / (rank + 1)
        ap += ((precision_0 + precision_1) * recall_step / 2)
    return ap


def mAP(kc):
    """计算mAP"""
    '''加载数据'''
    psi = np.loadtxt('./temp/psi_{}.csv'.format(kc))
    qid_x = mat73.loadmat('../data/qidx.mat')['qidx'].astype('int') - 1
    gnd = mat73.loadmat('../data/gnd.mat')['gnd']

    '''开始计算'''
    q = psi[qid_x]
    d = 128
    psi = psi[:, d:]
    q = q[:, d:]
    print("[ Results for varying powerlaw ]")
    for pw in [1.0, 0.7, 0.5, 0.3, 0.2, 0.0]:
        x_ = np.sign(psi) * np.power(np.abs(psi), pw)
        q_ = np.sign(q) * np.power(np.abs(q), pw)
        x_ /= np.linalg.norm(x_, axis=1, keepdims=True)
        x_ = np.nan_to_num(x_, copy=False)
        q_ /= np.linalg.norm(q_, axis=1, keepdims=True)
        q_ = np.nan_to_num(q_, copy=False)

        ranks, sim = my_nn(x_, q_, 1000)
        m_ap, aps = compute_map(ranks, gnd)

        print("Holidays k = {} d = {} pw = {:.2f} map = {:.3f}".format(kc, x_.shape[1], pw, m_ap))


if __name__ == '__main__':
    np.seterr(divide='ignore', invalid='ignore')
    mAP(config.k)
