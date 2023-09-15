def str2hms(hms_str):
    # คนื จ ำนวนชั่วโมง นำทีและวนิ ำที ที่ดึงมำจำกสตริง hms
    # เชน่ str2hms("10:03:29") ได้ 10,3,29
    t = hms_str.split(':')
    return int(t[0]),int(t[1]),int(t[2])

def hms2str(h,m,s):
    # คืนสตริงในรูปแบบ HH:MM:SS ที่น ำจ ำนวนชั่วโมง นำที และวินำทีมำจำก h,m และ s 
    # เชน่ hms2str(10,3,29) ได้ "10:03:29"
    return ('0'+str(h))[-2:] + ':' + ('0'+str(m))[-2:] + ':' + ('0'+str(s))[-2:]

def to_sec(h,m,s):
    # คืนจ ำนวนวินำทีทั้งหมดนับจำกเที่ยงคืนจำกถึงเวลำ h:m:s
    # เชน่ to_sec(10,3,29) ได้ 36209
    return h*60*60 + m*60 + s

def to_hms(s):
    # คืนจ ำนวนชั่วโมง นำที และวินำที ที่หำมำจำกจ ำนวนวินำที่ s ทั้งหมดนับจำกเที่ยงคืน
    # เชน่ to_hms(36209) ได้ 10,3,29
    h = s//60//60
    m = (s-h*60*60)//60 
    s = ((s-h*60*60)- m*60)
    return h ,m ,s

def diff(h1,m1,s1,h2,m2,s2):
    # คืนจ ำนวนชั่วโมง นำทีและวนิ ำที่ จะเป็นชว่ งเวลำตัง้แต่เวลำ h1,m1,s1 จนถึง h2,m2,s2
    # เชน่ diff(10,57,57, 12,0,0) ได้ 1,2,3
    # หมำยเหตุ เวลำ h1,m1,s1 ที่ได้รับ ไม่มำกกว่ำ h2,m2,s2 แน่ ๆ 
    # (เชน่ ไม่มีกรณีให้หำชว่ งเวลำตั้งแต่ 23,50,50 ถึง 2,1,1 แน่ ๆ)
    ds = (60 + (s2 - s1)) % 60
    if(s2 < s1):
        m2 -= 1

    dm = (60 + (m2 - m1)) % 60
    if(m2 < m1):
        h2 -= 1

    dh = (24 + (h2 - h1)) % 24
        
    return dh ,dm ,ds

def main():
    # ฟังกช์ ันนี้รับเวลำเริ่มต้น และเวลำสนิ้ สุด ในรูปแบบ HH:MM:SS
    # เพื่อแสดงชว่ งเวลำตั้งแต่เริ่มจนถึงสนิ้ สุด ในรูปแบบ HH:MM:SS
    # ดูตัวอย่ำงในตำรำงข้ำงล่ำง
    hms_start = input()
    hms_end = input()

    h1 ,m1 ,s1 = str2hms(hms_start)
    h2 ,m2 ,s2 = str2hms(hms_end)
    
    dh ,dm ,ds = diff(h1 ,m1 ,s1 ,h2 ,m2 ,s2)
    print(hms2str(dh ,dm ,ds))

exec(input()) # DON'T remove this line