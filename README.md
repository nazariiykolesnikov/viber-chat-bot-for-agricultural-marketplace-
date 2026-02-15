# 🌾 Viber Чат-бот для Аграрного маркетплейсу
Цей проєкт — багатоканальний чат‑бот для аграрного маркетплейсу

## Можливості, що підтримуються
- Відповідає на поширені запитання (FAQ); 
- Приймає заявки та повідомлення від користувачів; 
- Зберігає всі заявки у базі даних PostgreSQL; 
- Має адмін‑панель для перегляду та додавання заявок вручну; 
- Підтримує інтеграцію з Telegram та Viber;

## 📂 Структура проєкту 
├── public/
├── src/
    ├──── app/                    
          └── store.ts
    ├──── features/
          ├── auth/               
              ├── authSlice.ts
              ├── authApi.ts      
              ├── LoginPage.tsx
              └── RegisterPage.tsx
          └── dashboard/         
              └── DashboardPage.tsx
    ├──── components/             
          └── Navbar.tsx
    ├──── routes/                 
          └── AppRoutes.tsx
    ├──── utils/                  
          └── authGuard.tsx
    ├── main.tsx
- `app.py` — основний Flask‑додаток.
- `ApplicationModel` — ORM‑модель для таблиці заявок.
- `/chat` — REST API для веб‑чату.
- `/viber` — webhook для Viber‑бота.
- Telegram‑бот запускається у паралельному потоці
- `/admin/applications` — адмін‑панель для перегляду та додавання заявок.
