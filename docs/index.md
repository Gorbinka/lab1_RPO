# Документация проекта lab1_RPO

## Описание
Учебный проект по дисциплине «Технологии разработки программного обеспечения».

## Структура
- `person1/` — исходный код
- `tests/` — unit-тесты
- `.github/workflows/` — CI/CD

## Функции
- `add(a, b)` — сложение
- `multiply(a, b)` — умножение
- `divide(a, b)` — деление

## Запуск тестов
```bash
pytest -v

Создай `mkdocs.yml` в корне:

```bash
cat > mkdocs.yml << 'EOF'
site_name: lab1_RPO Documentation
nav:
  - Home: index.md
