def shouldGoToSchoolOrNot(weather, mood, health):
    if health == "bệnh":
        return "Không, có sức khỏe mới học được, không nên mạo hiểm."
    if weather == "mưa":
        if mood == "siêng":
            return "Có, nhưng nhớ mang áo mưa."
        else:
            return "Không, đi học trong lúc mưa rất mệt nếu bạn không có hứng thú"
    elif weather == "nắng":
        if mood == "siêng":
            return "Có, nên đi học."
        else:  
            return "Có, đi học luôn là ưu tiên"

    return "Vui lòng nhập lại."

def ask():
    print("Chào bạn! Mình sẽ giúp bạn quyết định có nên đi học không nhé!")
    weather = input("Thời tiết hôm nay thế nào? (nắng/mưa): ").strip().lower()
    mood = input("Tâm trạng của bạn thế nào? (siêng/lười): ").strip().lower()
    health = input("Sức khỏe của bạn ra sao? (khỏe/bệnh): ").strip().lower()
    return weather, mood, health 


weather, mood, health = ask()
decision = shouldGoToSchoolOrNot(weather, mood, health)
print("\nKết quả:", decision)
