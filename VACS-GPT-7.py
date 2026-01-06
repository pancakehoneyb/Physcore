import matplotlib.pyplot as plt
import numpy as np

G = 6.67430e-11  # Constante gravitacional em m³/(kg s²)

class Body3D:
    def __init__(self, name, mass, radius, position, velocity, color):
        self.name = name
        self.mass = mass
        self.radius = radius
        self.position = np.array(position)
        self.velocity = np.array(velocity)
        self.acceleration = np.zeros(3)
        self.color = color

def gravitational_force(body1, body2):
    r = body2.position - body1.position
    distance = np.linalg.norm(r)
    direction = r / distance
    force_magnitude = (G * body1.mass * body2.mass) / (distance ** 2)
    force = force_magnitude * direction
    return force

def update_bodies_acceleration(bodies):
    for i, body1 in enumerate(bodies):
        body1.acceleration = np.zeros(3)
        for j, body2 in enumerate(bodies):
            if i != j:
                force = gravitational_force(body1, body2)
                body1.acceleration += force / body1.mass

def update_bodies_velocity(bodies, dt):
    for body in bodies:
        body.velocity += body.acceleration * dt

def update_bodies_position(bodies, dt):
    for body in bodies:
        body.position += body.velocity * dt

def simulate_3d_bodies(bodies, total_time, instants_per_second, num_images):
    dt = 1 / instants_per_second
    total_instants = int(total_time * instants_per_second)
    positions = {i: [] for i in range(len(bodies))}

    for t in range(total_instants):
        update_bodies_acceleration(bodies)
        update_bodies_velocity(bodies, dt)
        update_bodies_position(bodies, dt)

        for i, body in enumerate(bodies):
            positions[i].append(body.position.copy())

    image_indices = [int(i * (total_instants - 1) / (num_images - 1)) for i in range(num_images)]
    image_indices = [min(idx, total_instants - 1) for idx in image_indices]  # Limit to valid indices

    return positions, image_indices

def main():
    num_bodies = int(input("Digite o número de corpos: "))
    bodies = []

    for i in range(num_bodies):
        name = input(f"Digite o nome do corpo {i + 1}: ")
        mass = float(input(f"Digite a massa do corpo {i + 1}: "))
        exp = int(input(f"Digite o expoente da massa do corpo {i + 1}: "))
        mass = mass * (10**exp)
        radius = float(input(f"Digite o raio do corpo {i + 1}: "))
        r = int(input(f"Digite o valor de R (0 a 255) para a cor do corpo {i + 1}: "))
        g = int(input(f"Digite o valor de G (0 a 255) para a cor do corpo {i + 1}: "))
        b = int(input(f"Digite o valor de B (0 a 255) para a cor do corpo {i + 1}: "))
        color = (r, g, b)
        position = [float(input(f"Digite as coordenadas (x, y, z) da posição inicial do corpo {i + 1}: ")) for _ in range(3)]
        velocity = [float(input(f"Digite as componentes (Vx, Vy, Vz) da velocidade inicial do corpo {i + 1}: ")) for _ in range(3)]

        body = Body3D(name=name, mass=mass, radius=radius, position=position, velocity=velocity, color=color)
        bodies.append(body)

    total_time = float(input("Digite o tempo total de simulação (em segundos): "))
    instants_per_second = int(input("Digite a quantidade de instantes por segundo: "))
    num_images = int(input("Digite o número de imagens a serem geradas: "))

    x_min = -7000000
    x_max = 7000000
    y_min = -7000000
    y_max = 7000000
    z_min = -7000000
    z_max = 7000000

    positions, image_indices = simulate_3d_bodies(bodies, total_time, instants_per_second, num_images)

    for j, image_index in enumerate(image_indices):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title(f'Movimentação dos Corpos - Instante: {image_index + 1}')

        for i, body in enumerate(bodies):
            x = positions[i][image_index][0]
            y = positions[i][image_index][1]
            z = positions[i][image_index][2]
            ax.scatter(x, y, z, label=body.name, s=body.radius*10, color=np.array(body.color)/255)

        ax.legend()

        ax.set_xlim(x_min, x_max)
        ax.set_ylim(y_min, y_max)
        ax.set_zlim(z_min, z_max)

        plt.savefig(f'corpos_instante_{j + 1}.png')
        plt.close()

if __name__ == "__main__":
    main()
