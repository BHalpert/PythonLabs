from Lab5 import Time
t1 = Time(1, 15, 30)
t2 = Time(5, 30, 20)
t3 = Time(10, 10, 10)
t4 = Time(13, 45, 25)
t5 = Time(16, 30, 0)
t6 = Time(20, 30, 45)

print(t1.gethours()), print(t1.getminutes()), print(t1.getseconds())
print(t2.gethours()), print(t2.getminutes()), print(t2.getseconds())

print(t1.tostring())
print(t3.tostring())
print(t5.tostring())

print(t1.timeinseconds())
print(t3.timeinseconds())
print(t5.timeinseconds())

t1.changethetime(2,2,2)
print(t1.tostring())
t1.changethetime(1,15,0)
print(t1.tostring())

print(t1.twelvehourclock())
print(t3.twelvehourclock())
print(t5.twelvehourclock())
print(t6.twelvehourclock())
t1.changethetime(23,15,0)
t2.changethetime(0,15,0)
print(t1.twelvehourclock())
print(t2.twelvehourclock())

print(t1.whattimeisit())
print(t3.whattimeisit())
print(t5.whattimeisit())

print(t1.compareto(t2))
print(t2.compareto(t1))
print(t3.compareto(t4))
print(t4.compareto(t3))
print(t5.compareto(t6))
print(t6.compareto(t5))

print(t2.timetill(t1).tostring())
print(t1.timetill(t2).tostring())
print(t3.timetill(t4).tostring())
print(t4.timetill(t3).tostring())
print(t5.timetill(t6).tostring())
print(t6.timetill(t5).tostring())

