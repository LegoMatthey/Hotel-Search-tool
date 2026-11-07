from flask import Flask, render_template, request, abort

app = Flask(__name__)

HOTELS = [
    {
        "id": 1, "name": "Отель Центральный", "city": "Москва",
        "address": "Тверская улица, 12", "price": 6500, "rating": 4.8,
        "description": "Уютный отель в центре Москвы, недалеко от достопримечательностей, кафе и станций метро.",
        "amenities": ["Wi-Fi", "Завтрак", "Кондиционер"],
    },
    {
        "id": 2, "name": "Московский дворик", "city": "Москва",
        "address": "Арбат, 18", "price": 5200, "rating": 4.7,
        "description": "Небольшой отель в спокойном переулке рядом с прогулочными улицами и кафе.",
        "amenities": ["Wi-Fi", "Уютный двор", "Завтрак"],
    },
    {
        "id": 3, "name": "City Park Hotel", "city": "Москва",
        "address": "Ленинградский проспект, 25", "price": 7100, "rating": 4.5,
        "description": "Современный отель с удобными номерами и быстрым доступом к общественному транспорту.",
        "amenities": ["Wi-Fi", "Парковка", "Завтрак"],
    },
    {
        "id": 4, "name": "Отель у парка", "city": "Москва",
        "address": "Улица Косыгина, 7", "price": 8300, "rating": 4.7,
        "description": "Комфортабельный вариант рядом с красивым парком. Подойдёт для спокойного отдыха.",
        "amenities": ["Wi-Fi", "Завтрак", "Парк"],
    },
    {
        "id": 5, "name": "Лайт Хаус", "city": "Москва",
        "address": "Садовая улица, 31", "price": 3900, "rating": 4.3,
        "description": "Простой и доступный отель с базовыми удобствами и удобным расположением.",
        "amenities": ["Wi-Fi", "Общая кухня"],
    },
    {
        "id": 6, "name": "Невский берег", "city": "Санкт-Петербург",
        "address": "Невский проспект, 44", "price": 5900, "rating": 4.8,
        "description": "Отель в исторической части Санкт-Петербурга, откуда удобно добираться до музеев и набережных.",
        "amenities": ["Wi-Fi", "Завтрак", "Кондиционер"],
    },
    {
        "id": 7, "name": "Северная звезда", "city": "Санкт-Петербург",
        "address": "Литейный проспект, 20", "price": 4300, "rating": 4.4,
        "description": "Небольшой городской отель с лаконичными номерами и спокойной атмосферой.",
        "amenities": ["Wi-Fi", "Кафе"],
    },
    {
        "id": 8, "name": "Петербургский уют", "city": "Санкт-Петербург",
        "address": "Улица Марата, 15", "price": 5100, "rating": 4.6,
        "description": "Уютное место для знакомства с городом, расположенное недалеко от центра.",
        "amenities": ["Wi-Fi", "Завтрак", "Прачечная"],
    },
    {
        "id": 9, "name": "Riverside Hotel", "city": "Санкт-Петербург",
        "address": "Набережная реки Фонтанки, 80", "price": 7800, "rating": 4.9,
        "description": "Современный отель с видом на город и удобными номерами для коротких поездок.",
        "amenities": ["Wi-Fi", "Ресторан", "Кондиционер"],
    },
    {
        "id": 10, "name": "Городской номер", "city": "Санкт-Петербург",
        "address": "Загородный проспект, 9", "price": 3500, "rating": 4.2,
        "description": "Бюджетный вариант размещения с необходимыми удобствами.",
        "amenities": ["Wi-Fi", "Общая кухня"],
    },
]

HOTELS_BY_ID = {hotel["id"]: hotel for hotel in HOTELS}

@app.route("/")
def index():
    return render_template(
        "index.html",
        page="home",
        hotels=HOTELS,
        hotel=None,
    )
    
@app.route("/hotel/<int:hotel_id>")
def hotel_detail(hotel_id):
    hotel = HOTELS_BY_ID.get(hotel_id)

    if hotel is None:
        abort(404)

    return render_template(
        "index.html",
        page="hotel",
        hotels=[],
        hotel=hotel,
    )
    
if __name__ == "__main__":
    app.run(debug=True)