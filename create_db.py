import pymongo
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["LahoreBadshah"]
menu_collection = db["menu"]

menu_data = [
    {
        "category": "Starter",
        "items": [
            {"name": "Chargha (full fried chicken)", "price": "8.00", "image_file": "/static/images/charga.jpg"},
            {"name": "Degi Chargha (steam roast -full chicken)", "price": "7.00", "image_file": "/static/images/deghi_chargha.jpg"},
            {"name": "Lahori Fish (fried)", "price": "17.00", "image_file": "/static/images/lahori_fish.jpg"},
            {"name": "Seekh Kebab", "price": "6.00", "image_file": "/static/images/seekh_kebab.jpg"},
            {"name": "Lamb Chops", "price": "8.50", "image_file": "/static/images/lamb_chops.jpg"},
            {"name": "Chicken Wings", "price": "5.00", "image_file": "/static/images/chicken_wings.jpg"},
            {"name": "Lamb Tikka", "price": "8.00", "image_file": "/static/images/lamb_tikka.jpg"},
            {"name": "Chicken Tikka", "price": "6.00", "image_file": "/static/images/chicken_tikka.jpg"},
            {"name": "Malai Botti", "price": "6.00", "image_file": "/static/images/malai_botti.jpg"},
            {"name": "Mixed Grill", "price": "18.00", "image_file": "/static/images/mixed_grill.jpg"}
        ]
    },
    {
        "category": "Lamb Dishes",
        "items": [
            {"name": "Fresh Lamb Karahi", "price": "25.00", "image_file": "/static/images/Lamb_karahi.jpg"},
            {"name": "Fresh Tomato Lamb Karahi", "price": "28.00", "image_file": "/static/images/Lamb_karahi1.jpg"},
            {"name": "Fresh Lamb Chilli Karahi", "price": "28.00", "image_file": "/static/images/Lamb_karahi.jpg"},
            {"name": "Fresh Lamb Butter Karahi", "price": "29.00", "image_file": "/static/images/Lamb_karahi.jpg"},
            {"name": "Hirn Karahi", "price": "12.00", "image_file": "/static/images/hiran_karahi.jpg"},
            {"name": "Fresh Hiran Karahi", "price": "32.00", "image_file": "/static/images/hiran_karahi.jpg"}
        ]
    },
    {
        "category": "Chicken Dishes",
        "items": [
            {"name": "Fresh Chicken Karahi", "price": "19.00", "image_file": "/static/images/chicken_karahi.jpg"},
            {"name": "Fresh Tomato Chicken Karahi", "price": "23.00", "image_file": "/static/images/chicken_karahi1.jpg"},
            {"name": "Fresh Chicken Chilli Karahi", "price": "23.00", "image_file": "/static/images/chicken_karahi.jpg"},
            {"name": "Fresh Chicken Butter Karahi", "price": "23.00", "image_file": "/static/images/chicken_karahi.jpg"},
            {"name": "Karailay Keema", "price": "7.00", "image_file": "/static/images/KarailayKeema.jpg"}
        ]
    },
    {
        "category": "Daily Special",
        "items": [
            {"name": "Lamb Curry", "price": "8.50", "image_file": "/static/images/Lamb_Curry.jpg"},
            {"name": "Chicken Curry", "price": "7.00", "image_file": "/static/images/chicken_curry.jpg"},
            {"name": "Lahori Chanay", "price": "6.00", "image_file": "/static/images/Chickpea_curry.jpg"}
        ]
    },
    {
        "category": "Lahori Special",
        "items": [
            {"name": "Lamb Paya", "price": "8.00", "image_file": "/static/images/Lamb_Paya.jpg"},
            {"name": "Hareesa", "price": "8.00", "image_file": "/static/images/Hareesa.jpg"},
            {"name": "Tawa Keema", "price": "9.00", "image_file": "/static/images/keema.jpg"},
            {"name": "Taka Tak", "price": "10.00", "image_file": "/static/images/taka_tak.jpg"},
            {"name": "Haleem", "price": "8.00", "image_file": "/static/images/Haleem.jpg"}
        ]
    },
    {
        "category": "Naan",
        "items": [
            {"name": "Naan", "price": "1.00", "image_file": "/static/images/Naan.jpg"},
            {"name": "Rogni Kulcha Naan", "price": "1.50", "image_file": "/static/images/r_naan.jpg"},
            {"name": "Roti", "price": "1.00", "image_file": "/static/images/Roti.jpg"}
        ]
    },
    {
        "category": "Salad Bar",
        "items": [
            {"name": "Fresh Pakistani Salad", "price": "2.50", "image_file": "/static/images/FreshPakistaniSalad.jpg"},
            {"name": "Raita", "price": "2.00", "image_file": "/static/images/Raita.jpg"}
        ]
    },
    {
        "category": "Drinks",
        "items": [
            {"name": "Soft Drink", "price": "1.20", "image_file": "/static/images/softdrink.jpg"},
            {"name": "Mango Lassi", "price": "7.00", "image_file": "/static/images/mangolassi.jpg"},
            {"name": "Dasi Lassi", "price": "6.00", "image_file": "/static/images/Lassi.jpg"},
            {"name": "Desi Tea", "price": "2.00", "image_file": "/static/images/tea.jpg"},
            {"name": "Twisto Bottle", "price": "2.00", "image_file": "/static/images/softdrink.jpg"}
        ]
    },
    {
        "category": "Curry Of The Day",
        "items": [
            {"name": "Palak Gosht", "price": "7.00", "image_file": "/static/images/PalakGosht.jpg"},
            {"name": "Daal Gosht", "price": "8.00", "image_file": "/static/images/DaalGosht.jpg"},
            {"name": "Chicken Biryani", "price": "7.00", "image_file": "/static/images/ChickenBiryani.jpg"},
            {"name": "Aloo Gosht", "price": "7.00", "image_file": "/static/images/AlooGosht.jpg"},
            {"name": "Bhindi Gosht", "price": "8.00", "image_file": "/static/images/BhindiGosht.jpg"},
            {"name": "Aloo Keema", "price": "7.00", "image_file": "/static/images/alooKeema.jpg"},
            {"name": "Lamb Curry", "price": "8.50", "image_file": "/static/images/Lamb_Curry.jpg"},
            {"name": "Chicken Curry", "price": "7.00", "image_file": "/static/images/Chicken_Curry.jpg"},
            {"name": "Lahori Channay", "price": "6.00", "image_file": "/static/images/Chickpea_curry.jpg"},
            {"name": "Daal Mash", "price": "6.00", "image_file": "/static/images/Daal_Mash.jpg"},
            {"name": "Daal Chana", "price": "6.00", "image_file": "/static/images/Daal_Chana.jpg"}
        ]
    },
    {
        "category": "Lunch Offers",
        "items": [
            {"name": "Karailay Keema", "price": "7.00", "image_file": "/static/images/KarailayKeema.jpg"},
            {"name": "Chicken Curry", "price": "8.00", "image_file": "/static/images/Chicken_Curry.jpg"},
            {"name": "Lahori Chanay", "price": "7.00", "image_file": "/static/images/Chickpea_curry.jpg"},
            {"name": "Chicken Biryani", "price": "7.00", "image_file": "//staticimages/ChickenBiryani.jpg"},
            {"name": "Daal Mash", "price": "8.00", "image_file": "/static/images/Daal_Mash.jpg"},
            {"name": "Daal Chana", "price": "7.00", "image_file": "/static/images/Daal_Chana.jpg"},
            {"name": "Palak Aloo", "price": "8.00", "image_file": "/static/images/Palak_Aloo.jpg"},
            {"name": "Hirn Karahi", "price": "32.00", "image_file": "/static/images/hiran_karahi.jpg"}
        ]
    },
    {
        "category": "Others",
        "items": [
            {"name": "Hirn Karahi", "price": "32.00", "image_file": "/static/images/hiran_karahi.jpg"},
            {"name": "Fresh Lamb Karahi", "price": "25.00", "image_file": "/static/images/Lamb_Karahi.jpg"},
            {"name": "Fresh Chicken Karahi", "price": "19.00", "image_file": "/static/images/chicken_karahi.jpg"},
            {"name": "Lahori Fish", "price": "17.00", "image_file": "/static/images/lahori_fish.jpg"},
            {"name": "Degi Chargha", "price": "7.00", "image_file": "/static/images/deghi_chargha.jpg"},
            {"name": "Special Mix Grill", "price": "18.00", "image_file": "/static/images/mixed_grill.jpg"}
        ]
    }
]

menu_collection.insert_many(menu_data)
print("Database created and data inserted successfully")
