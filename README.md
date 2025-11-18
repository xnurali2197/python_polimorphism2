# Library Book Management

Bu loyiha Python’da **Inkapsulyatsiya** va **Property** tushunchalarini amalda ko‘rsatish uchun yaratilgan. Loyihada kitoblarni boshqarish va foydalanuvchi-kutubxonachi rolini ajratish ko‘rsatiladi.

---

## Xususiyatlar

- **Book** klassi:
  - Kitob ma’lumotlari inkapsulyatsiya qilingan (`__title`, `__author`, `__pages`, `__is_available`).
  - Foydalanuvchi faqat `title` va `author` property orqali ko‘ra oladi.
  - Kutubxonachi (admin) quyidagi metodlar bilan ishlaydi:
    - `borrow()` – kitobni olish
    - `return_book()` – kitobni qaytarish
    - `is_available()` – kitob mavjudligini tekshirish

---

## Misol ishlatish

```python
# Kitob yaratish
book1 = Book("1984", "George Orwell", 328)

# Oddiy foydalanuvchi
print(book1.title)   # 1984
print(book1.author)  # George Orwell

# Kutubxonachi
book1.borrow()        # Kitobni oladi
print(book1.is_available())  # False
book1.return_book()   # Kitobni qaytaradi
print(book1.is_available())  # True
