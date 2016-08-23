from django.db import models


class Team(models.Model):
    teamid = models.AutoField(db_column='TeamID', primary_key=True) 
    team_name = models.CharField(db_column='TeamName', max_length=50) 

    class Meta:
        managed = True
        db_table = 'Team'
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'
        ordering = ('team_name',)

    def __str__(self):
        return self.team_name

class ReportingPeriod(models.Model):
    reporting_period_id = models.AutoField(db_column='ReportingPeriodID', primary_key=True) 
    start_date = models.DateField(db_column='StartDate')
    end_date = models.DateField(db_column='EndDate')

    class Meta:
        managed = True
        db_table = 'ReportingPeriod'
        verbose_name = 'Reporting Period'
        verbose_name_plural = 'Reporting Periods'
        ordering = ('start_date','end_date',)

    def __str__(self):
        return '{:%Y/%m/%d}'.format(self.start_date) + ' - ' + '{:%Y/%m/%d}'.format(self.end_date)

class CapacityMeasure(models.Model):
    capacity_measure_id = models.AutoField(db_column='CapacityMeasureID', primary_key=True) 
    team = models.ForeignKey('Team', models.DO_NOTHING, db_column='TeamID')
    reporting_period = models.ForeignKey('ReportingPeriod', models.DO_NOTHING, db_column='ReportingPeriodID')
    team_capacity_in_hours = models.DecimalField(db_column='TeamCapacityInHours', max_digits=5 ,decimal_places = 2)
    team_velocity_in_story_points = models.DecimalField(db_column='TeamVelocityInStoryPoints', max_digits=5, decimal_places = 2)
    team_FTE = models.DecimalField(db_column='TeamFTE',max_digits=5, decimal_places=1)
    class Meta:
        managed = True
        db_table = 'CapacityMeasure'
        verbose_name = 'Capacity Measure'
        verbose_name_plural = 'Capacity Measures'
        ordering = ('team__team_name','reporting_period__end_date',)

    def __str__(self):
        return '{:%Y/%m/%d}'.format(self.reporting_period.start_date) + ' - ' + self.team.team_name 