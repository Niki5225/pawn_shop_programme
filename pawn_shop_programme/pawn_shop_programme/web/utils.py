from pawn_shop_programme.web.models import EuroBought, EuroSold, OtherSold, OtherBought, PoundSold, PoundBought


def get_total_sum_euro_bought():
    total_sum = 0

    for euro in EuroBought.objects.all():
        total_sum += euro.course_bought * euro.quantity

    return -total_sum


def get_total_sum_euro_sold():
    total_sum = 0

    for euro in EuroSold.objects.all():
        total_sum += euro.course_sold * euro.quantity

    return total_sum


def get_total_sum_pound_bought():
    total_sum = 0

    for pound in PoundBought.objects.all():
        total_sum += pound.course_sold * pound.quantity

    return -total_sum


def get_total_sum_pound_sold():
    total_sum = 0

    for pound in PoundSold.objects.all():
        total_sum += pound.course_sold * pound.quantity

    return total_sum


def get_total_sum_other_values_bought():
    total_sum = 0

    for value in OtherBought.objects.all():
        total_sum += value.course_sold * value.quantity

    return -total_sum


def get_total_sum_other_values_sold():
    total_sum = 0

    for value in OtherSold.objects.all():
        total_sum += value.course_sold * value.quantity

    return total_sum


def get_total():
    return get_total_sum_euro_sold() + get_total_sum_euro_bought() + get_total_sum_pound_sold() + \
        get_total_sum_pound_bought() + get_total_sum_other_values_sold() + get_total_sum_other_values_bought()
