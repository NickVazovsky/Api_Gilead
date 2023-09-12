import os


def preview_upload_to(instance, filename):
    """
    Загрузка превью
    :param instance:
    :param filename:
    :return:
    """
    return os.path.join('preview/{0}'.format(instance.slug), instance.slug + os.path.splitext(filename)[1])


def material_upload_to(instance, filename):
    """
    Загрузка файла
    :param instance:
    :param filename:
    :return:
    """
    return os.path.join('material/{0}'.format(instance.slug), instance.slug + os.path.splitext(filename)[1])


def poster_upload_to(instance, filename):
    """
    Загрузка постера
    :param instance:
    :param filename:
    :return:
    """
    return os.path.join('posters/{0}'.format(instance.slug), instance.slug + os.path.splitext(filename)[1])
