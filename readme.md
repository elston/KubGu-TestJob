Computer vision test job for robotics laboratory of KubGu
========================================

Technology
----------------
- c++
- python
- docker


Description
----------------

### Задача 1 ([Решение](https://github.com/elston/KubGu-TestJob/blob/master/image/main/src/tz1/app.py))

ЯП: С++ или Python на выбор, консольная утилита, которая принимает на вход номер комнаты, и дает ответ. 

Вавилонцы решили построить удивительную башню — расширяющуюся к верху и содержащую бесконечное число этажей и комнат. Она устроена следующим образом — на первом этаже одна комната, затем идет два этажа на каждом из которых по две комнаты, затем идёт три этажа, на каждом из которых по три комнаты и так далее:

```
...
12 13 14
9 10 11
6 7 8
4 5
2 3
1
```

Эту башню решили оборудовать лифтом —- и вот задача: нужно научится по номеру комнаты определять, на каком этаже она находится и какая она по счету слева на этом этаже.

Входные данные: В первой строчке задан номер комнаты.

Выходные данные: Два целых числа — номер этажа и порядковый номер слева на этаже.

Пример:

```
Вход: 13
Выход: 6 2
Вход: 11
Выход: 5 3
```

### Задача 2 ([Решение](https://github.com/elston/KubGu-TestJob/blob/master/image/main/src/tz2/app_white.py)):

ЯП: приоритетно С++, можно Python

Дополнительно библиотека OpenCV

Поиск объектов по цвету. Реализовать алгоритм поиска объекта по цветовому патерну. 

В вашу программу будет отправлено фото стола для бильярда, на котором будет много шаров разного цвета, ваша задача найти и выделить белый шар. 

### Задача 3 ([Решение](https://github.com/elston/KubGu-TestJob/blob/master/image/main/src/tz3/app.py)): 

ЯП: приоритетно С++, можно Python 

Дополнительно библиотека OpenCV

Поиск обьекта по шаблону (части изображения). Ваша программа должна будет найти на фото объект изображенный на другом фото. Например вам будет дано Яблоко которое надо найти в натюрморте картины.


Getting Started with Docker and Docker Compose for Local Development
--------------------------------------------------------------------

### Install Docker

https://docs.docker.com/installation/

### Install Docker Compose

http://docs.docker.com/compose/install/

### Install the app's

In the project ./book (where the `Makefile` file is located), run:

#### 1. Build

```
make build
```

#### 2. bootstrap

```
make bootstrap
```

#### 3. run shell in contaner

```
make shell
```

#### 4. work on in contaner


```
workon main
ipython
>>> import cv2
>>> print(cv2.__version__)
3.3.0

```

.... It's work !!!