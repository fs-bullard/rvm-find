import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageOps

def compressed_sensing_plot():
    # 1) Load and preprocess image to 128x128 grayscale
    size = 800
    image = np.array(
        ImageOps.fit(
            Image.open('finch.png').convert('L'),
            (size, size),
            Image.LANCZOS
        )
    )

    # 2) Random subsampling (20% of pixels)
    np.random.seed(42)
    mask = np.random.rand(size, size) < 0.1
    subsampled = np.zeros_like(image)
    subsampled[mask] = image[mask]

    # 3) Compute full Fourier transform and magnitude
    ft = np.fft.fftshift(np.fft.fft2(image))
    magnitude = np.abs(ft)

    # 4) Keep only top 20% of modes by magnitude
    threshold = np.percentile(magnitude, 98)
    ft_top20 = ft * (magnitude >= threshold)

    # 5) Compute log magnitude for plotting
    ft_mag_top20 = np.log(np.abs(ft_top20) + 1)

    # 6) Placeholder for the reconstructed image
    reconstructed = image.copy()  # Replace with actual reconstruction

    # 7) Plot panels with arrows
    fig, axes = plt.subplots(1, 3, figsize=(9, 3))
    titles = [
        r'Measured Data, $\mathbf{y}$',
        r'Sparse coefficients, $\mathbf{\xi}$',
        r'Reconstruction, $\mathbf{x}$'
    ]
    data = [subsampled, ft_mag_top20, reconstructed]

    for ax, d, title in zip(axes, data, titles):
        ax.imshow(d, cmap='gray', interpolation='nearest')
        ax.set_title(title)
        ax.axis('off')

    fig.tight_layout(w_pad=2)
    plt.savefig(
        'cs_diagram.jpeg',
        dpi=600,            
        bbox_inches='tight',
        pad_inches=0.1,   
        transparent=True
    ) 
    # plt.show()



if __name__ == "__main__":
    plt.rcParams.update({
        "text.usetex":        True,                      # use LaTeX to render all text
        "font.family":        "serif", 
    })
    compressed_sensing_plot()