# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 23:45:30 2023

@author: jgila
"""
import matplotlib.pyplot as plt
import numpy as np
import math
from random import randrange
from random import choice



class particle():
    def __init__(self, mass, px, py, pz, vx, vy, vz, ax, ay, az, name=""):
        self.name = name
        self.mass = mass
        self.px = px
        self.py = py
        self.pz = pz
        self.vx = vx
        self.vy = vy
        self.vz = vz
        self.ax = ax
        self.ay = ay
        self.az = az
        
# sun = particle(2e30, 0,0,0, 0,0,0, 0,0,0,"sun")
# mercury = particle(3.285e23, 1,5.7e10,0, 4700000000,0,0, 0,0,0, "mercury")
# venus =particle(4.8e24, 0,1.1e11,0, 35000,0,0, 0,0,0, "venus")


# name_list = [sun.name, mercury.name, venus.name]
# part_list=[sun, mercury,venus ]
name_list = ["p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8", "p9", "p10"]
position_list = []
# name_list = ["p1","p2", "p3"]
# name_list = ["p1", "p2"]

for x in name_list:
    y = []
    position_list.append(y)

# for name in part_list:
#     y = []
#     position_list.append(y)




def get_particles_list(name_list):
    particles_list = []
    for x in range(len(name_list)):
        name = name_list[x]
        mass = randrange(start = 1, stop = 10,)
        while(mass==0):
            mass = randrange(start=1000)
        px = randrange(start=-100000, stop=100000, step = 1)
        py = randrange(start=-100000, stop=100000, step = 1)
        pz = randrange(start=-100000, stop=100000, step = 1)
        vx = randrange(start=-50000, stop=50000, step = 1)
        vy = randrange(start=-50000, stop=50000, step = 1)
        vz = randrange(start=-50000, stop=50000, step = 1)
        ax = randrange(start=-10000, stop=10000, step = 1)
        ay = randrange(start=-10000, stop=10000, step = 1)
        az = randrange(start=-10000, stop=10000, step = 1)
        newPart = particle(mass, px, py, pz, vx, vy, vz, ax, ay, az, name)
        particles_list.append(newPart)
        #print(newPart.px, newPart.py, newPart.pz)
    return particles_list

def calculate_grav_force(p1, p2):
    G = 1
    r = np.abs(math.sqrt((p1.px-p2.px)**2 + (p1.py - p2.py)**2 + (p1.pz - p2.pz)**2))
    #print(r)
    r_vector = ((p2.px-p1.px), (p2.py-p1.py), (p2.pz-p1.pz))
    # print(r_vector)
    Fg=[0,0,0]
    Fg[0] = (-G * (p2.mass)/((r_vector[0]+.001)**2))
    Fg[1] = (-G * (p2.mass)/((r_vector[1]+.001)**2))
    Fg[2] = (-G * (p2.mass)/((r_vector[2]+.001)**2))

    # p1.ax+=Fg*(p2.px-p1.px)
    # p1.ay+=Fg*(p2.py-p1.py)
    # p1.az+=Fg*(p2.pz-p1.pz)
    # print(Fg)
    return Fg


def update_acceleration(particle, particle_2):
    Fg = calculate_grav_force(particle, particle_2)
    particle.ax += Fg[0]/particle.mass
    particle.ay += Fg[1]/particle.mass
    particle.az += Fg[2]/particle.mass


def update_velocity(particle):
    particle.vx = particle.vx + particle.ax
    particle.vy = particle.vz + particle.ay
    particle.vz = particle.vz + particle.az


def update_position(particle):
    particle.px += particle.vx
    particle.py += particle.vy
    particle.pz += particle.vz


def output(particles_list, pos_list):
    i = 0
    for particle in particles_list:
        pos = (particle.px, particle.py, particle.pz)
        pos_list[i].append(pos)
        i += 1


def main(time):
    # particles_list = part_list

    particles_list = get_particles_list(name_list)
    for x in range(time):
        output(particles_list, position_list)
        for particle in particles_list:
            for particle_2 in particles_list:
                if particle.name != particle_2.name:
                    update_acceleration(particle, particle_2)
            update_velocity(particle)
            update_position(particle)


def plot_output(position_list, outfile=None):
    fig = plt.figure()
    colors = ['mediumpurple', 'darkgreen', 'orange', 'red', 'darkred', 'lightgreen', 'yellow', 'cyan', 'steelblue', 'peru', 'purple', 'blue', 'lime', 'saddlebrown', 'rosybrown', 'teal', 'deeppink']
    ax = fig.add_subplot(1, 1, 1, projection='3d')
    i=0
    for particle in position_list:
        x=[]
        y=[]
        z=[]
        for pos in particle:
            x.append(pos[0])
            y.append(pos[1])
            z.append(pos[2])
            

        ax.plot(x, y, z, c=choice(
            colors), label=name_list[i])
        i=i+1
    ax.legend()
    

    if outfile:
        plt.savefig(outfile)
    else:
        plt.show()


main(10)
#print(position_list)
plot_output(position_list)

# def animation(position_list):
#     for pos in  position_list :
#         position_list.set_data()
#         postition_list.set_3d_properties()



# position_list = [ax.plot([], [], "o-", markevery = 10000)[0] for _ in range()]

# anim3D = animation.FuncAnimation(fig, Animate3D, frames = n, interval = 30, blit = False)

# plt.show()