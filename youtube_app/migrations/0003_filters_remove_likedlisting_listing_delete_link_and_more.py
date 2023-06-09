# Generated by Django 4.1.7 on 2023-03-09 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("youtube_app", "0002_listing_video_likedlisting"),
    ]

    operations = [
        migrations.CreateModel(
            name="Filters",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "sortby",
                    models.CharField(
                        choices=[
                            ("Relevance", "Relevance"),
                            ("Upload Date", "Upload Date"),
                        ],
                        default=None,
                        max_length=24,
                    ),
                ),
                (
                    "features",
                    models.CharField(
                        choices=[
                            ("Live", "Live"),
                            ("Subtitles/CC", "Subtitles/CC"),
                            ("HD", "HD"),
                        ],
                        default=None,
                        max_length=24,
                    ),
                ),
                (
                    "duration",
                    models.CharField(
                        choices=[
                            ("< 4min", "< 4min"),
                            ("4-20 min", "4-20 min"),
                            ("> 20min", "> 20min"),
                        ],
                        default=None,
                        max_length=24,
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("Video", "Video"),
                            ("Channel", "Channel"),
                            ("Playlist", "Playlist"),
                        ],
                        default=None,
                        max_length=24,
                    ),
                ),
                (
                    "upload_date",
                    models.CharField(
                        choices=[
                            ("Last Hour", "Last Hour"),
                            ("Today", "Today"),
                            ("This Week", "This Week"),
                            ("This Month", "This Month"),
                            ("This Year", "This Year"),
                        ],
                        default=None,
                        max_length=24,
                    ),
                ),
            ],
        ),
        migrations.RemoveField(
            model_name="likedlisting",
            name="listing",
        ),
        migrations.DeleteModel(
            name="link",
        ),
        migrations.DeleteModel(
            name="Media",
        ),
        migrations.DeleteModel(
            name="Video",
        ),
        migrations.DeleteModel(
            name="LikedListing",
        ),
        migrations.DeleteModel(
            name="Listing",
        ),
    ]
