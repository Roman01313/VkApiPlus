import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType


def get_all_members(vk_session, group_id, count=1000, offset=0):
    members = []
    # Максимальное количество пользователей за один запрос (ограничение API)

    while True:
        response = vk_session.groups.getMembers(group_id=group_id, offset=offset, count=count)
        members.extend(response['items'])
        offset += count

        # Прерываем цикл, если количество пользователей меньше 'count', значит, мы получили все
        if offset >= response['count']:
            break

    return members

