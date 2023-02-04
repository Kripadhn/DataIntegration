import numpy as np
import random

def particle_filter(particles, weights, observations, motion_model, observation_model, resample_ratio=0.5):
    N = len(particles)
    
    # predict the new state of each particle
    particles = motion_model(particles)
    
    # update the weight of each particle based on the observed data
    weights = observation_model(particles, observations)
    weights = weights / sum(weights)
    
    # resample the particles to create a new set of particles
    new_particles = np.zeros((N, particles.shape[1]))
    indices = np.random.choice(N, size=N, p=weights)
    for i in range(N):
        new_particles[i] = particles[indices[i]]
    
    # add some random noise to the new particles to encourage exploration
    if resample_ratio < 1:
        noise_indices = np.random.choice(N, size=int(N * (1 - resample_ratio)), replace=False)
        for i in noise_indices:
            new_particles[i] = new_particles[i] + np.random.normal(0, 1, new_particles[i].shape)
    
    return new_particles, weights
