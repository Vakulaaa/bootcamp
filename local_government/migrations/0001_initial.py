from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='CouncilDecision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('council_name', models.CharField(max_length=180)),
                ('title', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=120)),
                ('status', models.CharField(choices=[('proposed', 'Proposed'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='proposed', max_length=20)),
                ('budget_amount', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('decision_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={'ordering': ['-decision_date', '-created_at']},
        ),
    ]
