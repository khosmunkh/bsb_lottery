from main.models import Lottery
code_mask = 'ICT11{:03d}'
code_range = 250
description = "Мега"
lotteries = []
for i in range(1, code_range + 1):
    code = code_mask.format(i)
    lotteries.append(
        Lottery(
            code=code,
            description=description
        )
    )
Lottery.objects.bulk_create(lotteries)

from main.models import Lottery
code_mask = 'ICT12{:03d}'
code_range = 250
description = "Молл"
lotteries = []
for i in range(1, code_range + 1):
    code = code_mask.format(i)
    lotteries.append(
        Lottery(
            code=code,
            description=description
        )
    )
Lottery.objects.bulk_create(lotteries)

from main.models import Lottery
code_mask = 'ICT13{:03d}'
code_range = 180
description = "Мега-2"
lotteries = []
for i in range(1, code_range + 1):
    code = code_mask.format(i)
    lotteries.append(
        Lottery(
            code=code,
            description=description
        )
    )
Lottery.objects.bulk_create(lotteries)

from main.models import Lottery
code_mask = 'ICT19{:03d}'
code_range = 20
description = "Гэрээт"
lotteries = []
for i in range(1, code_range + 1):
    code = code_mask.format(i)
    lotteries.append(
        Lottery(
            code=code,
            description=description
        )
    )
Lottery.objects.bulk_create(lotteries)
