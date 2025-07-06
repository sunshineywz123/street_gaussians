import numpy as np
from scipy.spatial.transform import Rotation as R

def affine_inverse(A: np.ndarray):
    R = A[..., :3, :3]  # ..., 3, 3
    T = A[..., :3, 3:]  # ..., 3, 1
    P = A[..., 3:, :]  # ..., 1, 4
    return np.concatenate([np.concatenate([R.T, -R.T @ T], axis=-1), P], axis=-2)

def rotate_extrinsic(novel_view_cam_info, angle_degrees, axis='z'):
    """
    旋转相机外参（4x4 变换矩阵）。

    参数:
    extrinsic_matrix (np.ndarray): 4x4 的相机外参变换矩阵。
    angle_degrees (float): 旋转角度，单位为度。
    axis (str): 旋转轴，可以是 'x', 'y' 或 'z'。

    返回:
    np.ndarray: 旋转后的相机外参变换矩阵。
    """
    ext = novel_view_cam_info.metadata['extrinsic']
    # 计算相机到世界的变换
    c2w = ext
    # 计算世界到相机的变换
    RT = affine_inverse(c2w)
    # 提取旋转矩阵
    Rotation = RT[:3, :3].T
    # 提取平移向量
    T = RT[:3, 3]
    # 提取旋转矩阵 (3x3)
    rotation_matrix = Rotation
    
    # 提取平移向量 (3x1)
    translation_vector = T
    # 将旋转矩阵转换为 scipy Rotation 对象
    rotation = R.from_matrix(rotation_matrix)

    # 创建绕指定轴旋转的旋转对象
    if axis == 'x':
        rotation_around_axis = R.from_euler('x', angle_degrees, degrees=True)
    elif axis == 'y':
        rotation_around_axis = R.from_euler('y', angle_degrees, degrees=True)
    elif axis == 'z':
        rotation_around_axis = R.from_euler('z', angle_degrees, degrees=True)
    else:
        raise ValueError("Invalid axis. Must be 'x', 'y', or 'z'.")

    # import ipdb; ipdb.set_trace()
    # 将原始旋转与绕轴旋转结合
    new_rotation =  rotation_around_axis*rotation 

    # 更新旋转矩阵
    rotated_matrix = new_rotation.as_matrix()

    # 创建新的 4x4 变换矩阵
    rotated_extrinsic_matrix = np.eye(4)
    rotated_extrinsic_matrix[:3, :3] = rotated_matrix
    rotated_extrinsic_matrix[:3, 3] = translation_vector

    # novel_view_cam_info.R = rotated_matrix
    
    # 更新新视角相机参数
    novel_view_cam_info = novel_view_cam_info._replace(
               R=rotated_matrix, T=translation_vector)
    return novel_view_cam_info
def main():
    # 示例 4x4 相机外参矩阵
    novel_view_cam_info = [None] * 12  # 创建一个包含12个元素的列表

    # 示例 4x4 相机外参矩阵
    extrinsic_matrix = np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])

    novel_view_cam_info[11] = {'extrinsic': extrinsic_matrix}

    # 旋转90度
    angle = 90.0
    axis = 'z'  # 绕Z轴旋转

    rotated_extrinsic_matrix = rotate_extrinsic(novel_view_cam_info, angle, axis)

    # 更新 novel_view_cam_info
    novel_view_cam_info[11]['extrinsic'] = rotated_extrinsic_matrix

    # 打印旋转后的旋转矩阵
    print("旋转后的 4x4 变换矩阵:")
    print(novel_view_cam_info[11]['extrinsic'])

if __name__ == "__main__":
    main()