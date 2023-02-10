from datetime import date, datetime, timedelta
from ics import Calendar, Event
from ics.grammar.parse import ContentLine
import event


class Events:
    def __init__(self):
        self.events = []

    def add_event(self, event_type, time, description, roles):
        index = 0
        if self.events[-1]:
            index = self.events[-1].index + 1
        event = Event(index, event_type, time, description, roles)
        self.events.append(event)

    def delete_event(self, index, event_type, time, description, roles):
        del self.events[index]

    def show(self):
        for event in self.events:
            event.show()


    def save(self, filename, events_to_save=None):
        """
        Example of using lessons_to_save:
        HtmlParser(3).parse('9303').save('test.ics', [Lesson.create(subject='Компьютерная графика')])
        :param filename:
        :param events_to_save:
        :return:
        """
        calendar = Calendar()
        monday = date.today() + timedelta(days=-date.today().weekday(), weeks=1)
        utc_timetable = ["5:00", "6:50", "8:40", "10:40", "12:30", "14:20", "16:05", "17:50"]
        events_to_save = ["""lesson.subject""" for lesson in events_to_save] if events_to_save else None
        for event in self.events:
            if not events_to_save or (events_to_save and event.subject in events_to_save):
                today = monday + timedelta(days=self.days.index(event.week_day)) + timedelta(
                    weeks=int(event.week) - 1)
                event = Event()
                event.name = f'{event.subject} | {event.teacher}'
                lesson_time = utc_timetable[event.lesson_index]
                lesson_begin = f'{today.strftime("%Y-%m-%d")} ' \
                               f'{lesson_time if len(lesson_time.split(":")[0]) != 1 else "0" + lesson_time}:00'
                event.begin = lesson_begin
                event.end = datetime.strftime(datetime.strptime(lesson_begin, '%Y-%m-%d %H:%M:%S') +
                                              timedelta(hours=1, minutes=35), '%Y-%m-%d %H:%M:%S')
                extra = ContentLine.parse('RRULE:FREQ=WEEKLY;INTERVAL=2')
                event.extra.append(extra)
                calendar.events.add(event)
        with open(filename, 'w', encoding='utf-8') as file:
            file.writelines(calendar)

    # The function of loading the schedule from a file
    def load(cls, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            calendar = Calendar(file.read())
        monday = date.today() + timedelta(days=-date.today().weekday(), weeks=1)
        manager = cls()
        for event in calendar.events:
            week = '2' if datetime.strptime(event.begin.strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S') > \
                          datetime.combine(monday + timedelta(weeks=1), datetime.min.time()) else '1'
            lesson_begin = event.begin.strftime('%H:%M')
            lesson_index = cls.timetable.index(lesson_begin if lesson_begin[0] != '0' else lesson_begin[1:])
            week_day = cls.days[event.begin.weekday()]
            teacher = event.name.split(' | ')[-1]
            subject = event.name.split(' | ')[0]
            manager.add_lesson(subject, week, week_day, lesson_index, teacher=teacher)
        return manager



