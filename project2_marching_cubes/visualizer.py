import numpy as np
import plotly.graph_objects as go
from skimage import measure

# Generate a sphere to display
grid_size = 64
x, y, z = np.ogrid[-1:1:grid_size*1j, -1:1:grid_size*1j, -1:1:grid_size*1j]

sphere = (x**2 + y**2 +z**2)

# Use the marching cubes algorithm to get the vertices and faces
radius = 0.5
vertices, faces, _, _ = measure.marching_cubes(sphere, radius**2)

# Vertex coordinates
x_coords = vertices[:, 0]
y_coords = vertices[:, 1]
z_coords = vertices[:, 2]

# Triangle face vertex indices
v0 = faces[:, 0]
v1 = faces[:, 1]
v2 = faces[:, 2]

# Create the plotly mesh
plotly_mesh = go.Mesh3d(
    x=x_coords,
    y=y_coords,
    z=z_coords,
    i=v0,
    j=v1,
    k=v2,
    color="red"
    )

# Show the model
fig = go.Figure(data=plotly_mesh)
fig.update_layout(title="Marching Cubes Example")
fig.show()

# Save plotly figure to html file
fig.write_html("example.html")