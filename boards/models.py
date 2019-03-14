from django.db import models

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.id}: {self.title}"
        return  self.title
        
class Comment(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return  self.content
    
    # on_delete
    # 참조하는 부모객체가 사라졌을때, 부모에 딸려있는 자식 객체들을 어떻게 처리할지 정의한다.
    
    # 데이터베이스 무결성
    # 1. 개체 무결성: PK / NOT NULL / UNIQUE
    #     - 식별자는 NULL일 수 없고 중복일 수 없다.
    # 2. 참조 무결성 : FK / 모든 외래 키의 값은 2가지 상태 가운데 하나에만 속함을 규정
    # 3. 범위 / 도메인 무결성 : 컬럼은 지정된 형식을 반드시 만족해야 한다. (CharField, TextField , ..)
    
    # on_delete 속성 값
    # 1. CASCADE : 부모객체가 삭제됐을 때 이를 참조하는 객체도 삭제한다. (댓글 삭제 시 답댓 같이 삭제)
    # 2. PROTECT : 참조가 되어있는경우 삭제 시도 시 오류 발생(답댓 달리면 원 댓글 삭제 안됨)
    # 3. SET NULL : 부모객체가 삭제됐을 때 참조하는 모든 값을 NULL로 치환(NOT NULL 조건시 사용 불가능)
    # 4. SET_DEFAULT : 모든 값이 DEFAULT로 치환
    # 5. SET() : 특정 함수 호출
    # 6. DO_NOTHING : 아무것도 하지 않음.(원댓만 사라지고 답댓 남아있음) 다만 SQL에서는 on_delete를 직접 설정해줘야 함
    
