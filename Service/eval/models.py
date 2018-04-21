from django.core.validators import validate_comma_separated_integer_list
from django.db import models

from user.models import UserProfile


class Scale(models.Model):
    title = models.CharField(max_length=100, blank=False)
    introduction = models.TextField(null=True, blank=True)
    thumbnail = models.ImageField(null=True, blank=True, default=None, upload_to='static/images/thumb')
    is_top = models.BooleanField('置顶', default=False)
    created = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'eval_scale'
        ordering = ['-created']

    def __str__(self):
        return str(self.title)


class ScaleOption(models.Model):
    # scale = models.ForeignKey(Scale, on_delete=models.CASCADE)
    key = models.IntegerField(blank=False, null=False, default=1)
    value = models.CharField(max_length=100, blank=False)
    score = models.IntegerField(default=1)

    class Meta:
        db_table = 'eval_option'

    def __str__(self):
        return str(self.value)


class ScaleItem(models.Model):
    scale = models.ForeignKey(Scale, on_delete=models.CASCADE)
    sn = models.IntegerField(default=1)
    question = models.TextField()

    # opts = models.ManyToManyField(to=ScaleOption)

    class Meta:
        db_table = 'eval_item'

    def __str__(self):
        return str(self.question[:20] + '...')


class ScaleResult(models.Model):
    scale = models.ForeignKey(Scale, on_delete=models.CASCADE)
    key = models.CharField(max_length=100, blank=False)
    value = models.CharField(max_length=100, blank=False)

    class Meta:
        db_table = 'eval_result'


class ScaleItemOpt(models.Model):
    # 一个问题 -> 多个答案， 不同程度的对应不同的结果
    question = models.ForeignKey(to=Scale, on_delete=models.CASCADE)
    opt = models.ForeignKey(to=ScaleOption, on_delete=models.CASCADE)
    # opts = models.ManyToManyField(to=ScaleOption)
    bonus = models.ForeignKey(ScaleResult, on_delete=models.CASCADE)

    class Meta:
        db_table = 'eval_item_opts'

    def __str__(self):
        return str(self.question[:20] + '...')


class ScaleConclusion(models.Model):
    scale = models.ForeignKey(Scale, on_delete=models.CASCADE)
    key = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=False)

    class Meta:
        db_table = 'eval_conclusion'


# class ScaleCorrespond(models.Model):
#     scale = models.ForeignKey(Scale, on_delete=models.CASCADE)
#     result = models.ForeignKey(ScaleResult, on_delete=models.CASCADE)
#     opts = models.ForeignKey('选项与结果对应关系', max_length=1000, validators=[validate_comma_separated_integer_list])
#
#     class Meta:
#         db_table = 'eval_option_result'


class ScaleRecord(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.DO_NOTHING)
    scale = models.ForeignKey(Scale, on_delete=models.CASCADE)
    chose = models.CharField('已选', max_length=1000, validators=[validate_comma_separated_integer_list])
    final = models.CharField('最终结果', max_length=50)
    fin_con = models.ForeignKey(ScaleConclusion, on_delete=models.CASCADE)

    class Meta:
        db_table = 'eval_record'
