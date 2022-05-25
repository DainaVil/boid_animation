# Лабораторная работа 3.2. Сложная анимация
## Цель работы
Цель выполнения задач из данного списка - применить полученные навыки работы с графикой и анимацией для выполнения более сложных проектов.   
Каждая задача предполагает продумывание структуры программы, то есть этап проектирования. 

## Задание

### Бойды (165)

Реализуйте известный алгоритм "бойды", симулирующий стайное проведение птиц и других животных. Используйте набор бойдов со случайными положением и случайной, но органичной начальной скоростью.
1. Добавьте возможность включить или отключать каждую из трёх входящих в алгоритм сил, например, по нажатию кнопки клавиатуры 
2. Позвольте пользователю регулировать весе этих трёх сил, например при помощи слайдеров.

## Реализация
Использована библиотека PyGame 2.1.2.
## Управление игрой 
Зажать первую букву названия силы (a - alignment, s - separation, c - cohesion) и клавишу:  
\- (минус) для уменьшения силы  
=/+ для увеличения силы  
1 для включения значения силы по умолчанию  
0 для полного отключения силы  

## Структура файлов
├─ README.md  
├─ boid.py  
├─ main.py  


