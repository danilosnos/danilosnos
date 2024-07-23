from matplotlib import image
import matplotlib.pyplot as plt
import numpy as np

# Загрузим изображение
image_path = 'your_image_path.jpg'  # Замените на путь к вашему изображению
img_array = image.imread(image_path)
print(img_array.shape, img_array.dtype)

# Удалим Alpha слой, оставим только RGB
img_array = img_array[..., 0:3]

# Определим цвета в RGB
red = np.array([255, 0, 0], dtype=np.uint8)
green = np.array([0, 255, 0], dtype=np.uint8)

# Найдем пиксели звезды и флага
star_mask = np.all(img_array == [0, 0, 255], axis=-1)  # Синий цвет
flag_mask = np.all(img_array == [255, 255, 255], axis=-1)  # Белый цвет (предполагаем, что флаг белый)

# Покрасим звезду в красный цвет
img_array[star_mask] = red

# Покрасим флаг в зеленый цвет
img_array[flag_mask] = green

# Отобразим результат
plt.imshow(img_array)
plt.show()
