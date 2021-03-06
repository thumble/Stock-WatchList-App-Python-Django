from django.db import models

# Create your models here.

class User(models.Model):
    userId = models.AutoField(auto_created=True, primary_key=True, serialize=False, max_length=20)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name + ":" + str(self.userId) + "<"+ self.email +">"

class Watch(models.Model):
    watchId = models.AutoField(auto_created=True, primary_key=True, serialize=False, max_length=20)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    watchName = models.CharField(max_length=50)

    def __str__(self):
        return self.watchName + "<" + str(self.watchId) + ">"

class Asset(models.Model):
    assetId = models.AutoField(auto_created=True, primary_key=True, serialize=False, max_length=20)
    assetName = models.CharField(max_length=50)
    open = models.CharField(max_length=50)
    close = models.CharField(max_length=50)
    volume = models.IntegerField(default=0.0)
    high = models.CharField(max_length=50)
    low = models.CharField(max_length=50)
    adjClose = models.CharField(max_length=50)
    date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.assetName + "<" + str(self.assetId) + ">"

class WatchAsset(models.Model):
    watchAssetId = models.AutoField(auto_created=True, primary_key=True, serialize=False, max_length=20)
    watchId = models.ForeignKey(Watch, on_delete=models.CASCADE)
    assetId = models.ForeignKey(Asset, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['watchId', 'assetId']

    def __str__(self):
        return str(self.watchId) + ':' + str(self.assetId)
