import distance
import circle
import operations
import favorite_movies
import my_family
import zoo
import songs_list
import secret
import garden
import shopping
import store




def main():
    print('ВЫБЕРИТЕ НОМЕР ЗАДАНИЯ:')



    vibor = (input('Введите число:'))

    if vibor == '0':
        distance.goroda()
    elif vibor == '1':
        circle.ploshad()
    elif vibor == '2':
        operations.operations()
    elif vibor == '3':
        favorite_movies.movies()
    elif vibor == '4':
        my_family.semia()
    elif vibor == '5':
        zoo.run_zoo()
    elif vibor == '6':
        songs_list.pesnia()
    elif vibor == '7':
        secret.soobshenie()
    elif vibor == '8':
        garden.swetok()
    elif vibor == '9':
        shopping.magazine()
    elif vibor == '10':
        store.mebel()
    else:
        print('Такого числа нет в списке')

main()