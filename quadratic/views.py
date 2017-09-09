from django.shortcuts import render
import math

from quadratic.forms import QuadraticForm


def quadratic_result(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    c = request.GET.get('c')
    form = QuadraticForm(initial={'a': a, 'b': b, 'c': c})
    form.a = a
    form.b = b
    form.c = c
    form.is_valid()
    is_valid = True

    if 0 == len(a):
        a = 'коэффициент не определен'
        is_valid = False
    elif not a.isdigit():
        if a.startswith('-') and a[1:].isdigit():
            a = a
        else:
            a += ' коэффициент не целое число'
            is_valid = False
    elif 0 == int(a):
        a += ' коэффициент при первом слагаемом уравнения не может быть равным нулю'
        is_valid = False

    if 0 == len(b):
        b = 'коэффициент не определен'
        is_valid = False
    elif not b.isdigit():
        if b.startswith('-') and b[1:].isdigit():
            b = b
        else:
            b += ' коэффициент не целое число'
            is_valid = False
    if 0 == len(c):
        c = 'коэффициент не определен'
        is_valid = False
    elif not c.isdigit():
        if c.startswith('-') and c[1:].isdigit():
            c = c
        else:
            c += ' коэффициент не целое число'
            is_valid = False

    result_descr = result = ''
    if is_valid:
        a = int(a)
        b = int(b)
        c = int(c)
        discr = b ** 2 - 4 * a * c
        if discr > 0:
            x1 = (-b + math.sqrt(discr)) / (2 * a)
            x2 = (-b - math.sqrt(discr)) / (2 * a)
            result = 'Квадратное уравнение имеет два действительных корня: x1 = %.1f, x2 = %.1f' % (x1, x2)
        elif discr == 0:
            x1 = -b / (2 * a)
            result = 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %.1f' % x1
        else:
            result = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
        result_descr = 'Дискриминант: %d' % discr

    return render(
        request,
        'quadratic/results.html',
        {
            'a': a,
            'b': b,
            'c': c,
            'result': result,
            'result_descr': result_descr,
            'form': form
        }
    )
