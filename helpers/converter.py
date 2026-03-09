import pandas as pd
import numpy as np

def convert_sd_to_EN(
        path_df: pd.DataFrame, 
        track_csv_path: str = '../data/track_centerline.csv'
    ) -> pd.DataFrame:
    # Load track centerline
    track_df = pd.read_csv(track_csv_path)
    track_df = track_df.sort_values('s').reset_index(drop=True)

    all_s = track_df['s'].values
    all_E = track_df['E'].values
    all_N = track_df['N'].values
    nx = track_df['nx'].values
    ny = track_df['ny'].values

    path_s = path_df['s'].values
    path_d = path_df['d'].values

    track_E_interp = np.interp(path_s, all_s, all_E)
    track_N_interp = np.interp(path_s, all_s, all_N)
    normal_x = np.interp(path_s, all_s, nx)
    normal_y = np.interp(path_s, all_s, ny)

    path_E = track_E_interp + normal_x * path_d
    path_N = track_N_interp + normal_y * path_d

    output_df = path_df.copy()
    output_df['E'] = path_E
    output_df['N'] = path_N

    cols = ['E', 'N'] + [col for col in output_df.columns if col not in ['E', 'N']]
    return output_df[cols]
