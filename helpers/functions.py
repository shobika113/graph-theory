import numpy as np
import constants as vh

def compute_resistive_force(v):
    F_drag = 0.5 * vh.RHO * vh.CD_A * v**2
    F_roll = vh.M * vh.G * vh.C_R
    return F_drag + F_roll

def compute_h2_consumption(a_net, v1, v2, arc_length):
    a_net = np.asarray(a_net, float)
    v1 = np.asarray(v1, float)
    v2 = np.asarray(v2, float)
    arc_length = np.asarray(arc_length, float)

    m_eff = vh.M * (1 + vh.LAMBDA_INERTIA)
    v_avg = np.maximum((v1 + v2) / 2.0, 1e-6)

    F_res = compute_resistive_force(v_avg)
    E_res = F_res * arc_length

    dE_kin = 0.5 * m_eff * (v2**2 - v1**2)
    E_acc = np.maximum(dE_kin, 0.0)

    E_required = (E_res + E_acc) / vh.ETA_FC
    m_H2_edge = E_required / vh.LHV_H2
    return m_H2_edge

def compute_cost(m_H2_edge, v, v_target):
    W_VELOCITY_PENALTY = 1e-5
    vpen = (np.maximum(v_target - v, 0.0))**2
    return m_H2_edge + W_VELOCITY_PENALTY * vpen

def compute_edge_costs(a_net, v1, v2, arc_length, v_target):
    m_H2_edge = compute_h2_consumption(a_net, v1, v2, arc_length)
    v = (v1 + v2) / 2.0
    cost = compute_cost(m_H2_edge, v, v_target)
    return cost, m_H2_edge
