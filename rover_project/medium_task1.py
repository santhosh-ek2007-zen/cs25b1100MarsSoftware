import math

def rotation_matrix(rx, ry, rz):
    # Convert degrees to radians
    rx = math.radians(rx)
    ry = math.radians(ry)
    rz = math.radians(rz)

    # Rotation matrices
    Rx = [
        [1, 0, 0],
        [0, math.cos(rx), -math.sin(rx)],
        [0, math.sin(rx), math.cos(rx)]
    ]

    Ry = [
        [math.cos(ry), 0, math.sin(ry)],
        [0, 1, 0],
        [-math.sin(ry), 0, math.cos(ry)]
    ]

    Rz = [
        [math.cos(rz), -math.sin(rz), 0],
        [math.sin(rz), math.cos(rz), 0],
        [0, 0, 1]
    ]

    # Matrix multiply: R = Rz * Ry * Rx
    def matmul(A, B):
        result = [[0]*3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    result[i][j] += A[i][k] * B[k][j]
        return result

    R = matmul(Rz, matmul(Ry, Rx))
    return R


def transform_to_world(p_cam, rover_pos, rover_rot):
    R = rotation_matrix(*rover_rot)

    # Apply rotation
    x = R[0][0]*p_cam[0] + R[0][1]*p_cam[1] + R[0][2]*p_cam[2]
    y = R[1][0]*p_cam[0] + R[1][1]*p_cam[1] + R[1][2]*p_cam[2]
    z = R[2][0]*p_cam[0] + R[2][1]*p_cam[1] + R[2][2]*p_cam[2]

    # Apply translation
    x += rover_pos[0]
    y += rover_pos[1]
    z += rover_pos[2]

    return (x, y, z)


# Example input
p_cam = (2, 1, 3)
rover_pos = (10, 5, 0)
rover_rot = (0, 0, 45)

result = transform_to_world(p_cam, rover_pos, rover_rot)
print(result)