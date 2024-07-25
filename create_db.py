import pymongo
from pymongo import MongoClient

client = MongoClient("mongodb+srv://admin:admin@mycluster.w4b9g4s.mongodb.net/?retryWrites=true&w=majority&appName=MYCluster/epic-api")
db = client["LahoreBadshah"]
menu_collection = db["menu"]

menu_data = [
    {
        "category": "Starter",
        "items": [
            {"name": "Chargha ", "price": "8.00", "image_file": "Chargha.jpg"},
            {"name": "Deghi Chargha ", "price": "7.00", "image_file": "deghi chargha.jpg"},
            {"name": "Lahori Fish", "price": "17.00", "image_file": "lahori_fish.jpg"},
            {"name": "Seekh Kebab", "price": "6.00", "image_file": "seekh_kabab.jpg"},
            {"name": "Lamb Chops", "price": "8.50", "image_file": "lamb_chops.jpg"},
            {"name": "Chicken Wings", "price": "5.00", "image_file": "chicken_wings.jpg"},
            {"name": "Lamb Tikka", "price": "8.00", "image_file": "lamb_tikka.jpg"},
            {"name": "Chicken Tikka", "price": "6.00", "image_file": "chicken_tikka.jpg"},
            {"name": "Malai Botti", "price": "6.00", "image_file": "malai_botti.jpg"},
            {"name": "Mixed Grill", "price": "18.00", "image_file": "mixed_grill.jpg"}
        ]
    },
    {
        "category": "Lamb Dishes",
        "items": [
            {"name": "Fresh Lamb Karahi", "price": "25.00", "image_file": "Lamb_karahi.jpg"},
            {"name": "Fresh Tomato Lamb Karahi", "price": "28.00", "image_file": "Lamb_karahi1.jpg"},
            {"name": "Fresh Lamb Chilli Karahi", "price": "28.00", "image_file": "Lamb_karahi.jpg"},
            {"name": "Fresh Lamb Butter Karahi", "price": "29.00", "image_file": "Lamb_karahi.jpg"},
            {"name": "Hirn Karahi", "price": "12.00", "image_file": "hiran_karahi.jpg"},
            {"name": "Fresh Hiran Karahi", "price": "32.00", "image_file": "hiran_karahi.jpg"}
        ]
    },
    {
        "category": "Chicken Dishes",
        "items": [
            {"name": "Fresh Chicken Karahi", "price": "19.00", "image_file": "chicken_karahi.jpg"},
            {"name": "Fresh Tomato Chicken Karahi", "price": "23.00", "image_file": "chicken_karahi1.jpg"},
            {"name": "Fresh Chicken Chilli Karahi", "price": "23.00", "image_file": "chicken_karahi.jpg"},
            {"name": "Fresh Chicken Butter Karahi", "price": "23.00", "image_file": "chicken_karahi.jpg"},
            {"name": "Karailay Keema", "price": "7.00", "image_file": "KarailayKeema.jpg"}
        ]
    },
    {
        "category": "Daily Special",
        "items": [
            {"name": "Lamb Curry", "price": "8.50", "image_file": "Lamb_Curry.jpg"},
            {"name": "Chicken Curry", "price": "7.00", "image_file": "chicken_curry.jpg"},
            {"name": "Lahori Chanay", "price": "6.00", "image_file": "Chickpea_curry.jpg"}
        ]
    },
    {
        "category": "Lahori Special",
        "items": [
            {"name": "Lamb Paya", "price": "8.00", "image_file": "Lamb_Paya.jpg"},
            {"name": "Hareesa", "price": "8.00", "image_file": "Hareesa.jpg"},
            {"name": "Tawa Keema", "price": "9.00", "image_file": "keema.jpg"},
            {"name": "Taka Tak", "price": "10.00", "image_file": "taka_tak.jpg"},
            {"name": "Haleem", "price": "8.00", "image_file": "Haleem.jpg"}
        ]
    },
    {
        "category": "Naan",
        "items": [
            {"name": "Naan", "price": "1.00", "image_file": "Naan.jpg"},
            {"name": "Rogni Kulcha Naan", "price": "1.50", "image_file": "r_naan.jpg"},
            {"name": "Roti", "price": "1.00", "image_file": "Roti.jpg"}
        ]
    },
    {
        "category": "Salad Bar",
        "items": [
            {"name": "Fresh Pakistani Salad", "price": "2.50", "image_file": "FreshPakistaniSalad.jpg"},
            {"name": "Raita", "price": "2.00", "image_file": "Raita.jpg"}
        ]
    },
    {
        "category": "Drinks",
        "items": [
            {"name": "Soft Drink", "price": "1.20", "image_file": "softdrink.jpg"},
            {"name": "Mango Lassi", "price": "7.00", "image_file": "mangolassi.jpg"},
            {"name": "Dasi Lassi", "price": "6.00", "image_file": "Lassi.jpg"},
            {"name": "Desi Tea", "price": "2.00", "image_file": "tea.jpg"},
            {"name": "Twisto Bottle", "price": "2.00", "image_file": "softdrink.jpg"}
        ]
    },
    {
        "category": "Curry Of The Day",
        "items": [
            {"name": "Palak Gosht", "price": "7.00", "image_file": "PalakGosht.jpg"},
            {"name": "Daal Gosht", "price": "8.00", "image_file": "DaalGosht.jpg"},
            {"name": "Chicken Biryani", "price": "7.00", "image_file": "ChickenBiryani.jpg"},
            {"name": "Aloo Gosht", "price": "7.00", "image_file": "Aloo Gosht.jpg"},
            {"name": "Bhindi Gosht", "price": "8.00", "image_file": "Bhindi Gosht.jpg"},
            {"name": "Aloo Keema", "price": "7.00", "image_file": "Aloo Keema.jpg"},
            {"name": "Lamb Curry", "price": "8.50", "image_file": "Lamb_Curry.jpg"},
            {"name": "Chicken Curry", "price": "7.00", "image_file": "Chicken_Curry.jpg"},
            {"name": "Lahori Channay", "price": "6.00", "image_file": "Chickpea_curry.jpg"},
            {"name": "Daal Mash", "price": "6.00", "image_file": "Daal_Mash.jpg"},
            {"name": "Daal Chana", "price": "6.00", "image_file": "Daal_Chana.jpg"}
        ]
    },
    {
        "category": "Lunch Offers",
        "items": [
            {"name": "Karailay Keema", "price": "7.00", "image_file": "KarailayKeema.jpg"},
            {"name": "Chicken Curry", "price": "8.00", "image_file": "Chicken_Curry.jpg"},
            {"name": "Lahori Chanay", "price": "7.00", "image_file": "Chickpea_curry.jpg"},
            {"name": "Chicken Biryani", "price": "7.00", "image_file": "ChickenBiryani.jpg"},
            {"name": "Daal Mash", "price": "8.00", "image_file": "Daal_Mash.jpg"},
            {"name": "Daal Chana", "price": "7.00", "image_file": "Daal_Chana.jpg"},
            {"name": "Palak Aloo", "price": "8.00", "image_file": "Palak_Aloo.jpg"},
            {"name": "Hirn Karahi", "price": "32.00", "image_file": "hiran_karahi.jpg"}
        ]
    },
    {
        "category": "Others",
        "items": [
            {"name": "Hirn Karahi", "price": "32.00", "image_file": "hiran_karahi.jpg"},
            {"name": "Fresh Lamb Karahi", "price": "25.00", "image_file": "Lamb_Karahi.jpg"},
            {"name": "Fresh Chicken Karahi", "price": "19.00", "image_file": "chicken_karahi.jpg"},
            {"name": "Lahori Fish", "price": "17.00", "image_file": "lahori_fish.jpg"},
            {"name": "Degi Chargha", "price": "7.00", "image_file": "deghi chargha.jpg"},
            {"name": "Special Mix Grill", "price": "18.00", "image_file": "mixed_grill.jpg"}
        ]
    }
]

menu_collection.insert_many(menu_data)
print("Database created and data inserted successfully")
