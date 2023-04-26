def quicksort(palavra):
    if len(palavra) <= 1:
        return palavra
    else:
        pivot = palavra[-1]
        menores = []
        maiores = []
        iguais = []
        for letra in palavra:
            if letra < pivot:
                menores.append(letra)
            elif letra > pivot:
                maiores.append(letra)
            else:
                iguais.append(letra)
        return (
            quicksort("".join(menores))
            + "".join(iguais)
            + quicksort("".join(maiores))
        )


def is_anagram(first_string, second_string):
    if not first_string and not second_string:
        return (first_string, second_string, False)
    primeira, segunda = quicksort(first_string.lower()), quicksort(
        second_string.lower()
    )
    if primeira == segunda:
        return (primeira, segunda, True)
    else:
        return (primeira, segunda, False)
