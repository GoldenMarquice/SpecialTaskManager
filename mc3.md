# Mini Challenge 3

## Issue management

### Acceptance Criteria

1. Implement full CRUD support for Tasks.
2. Create a task model with the attributes shown below (note 1)
3. Create a status model with the attributes shown below (note 2)
4. Generate a view that shows tasks that are in the "to do", "in progress" and "done" status.

### Note 1
```
class Task(models.Model):
    summary = models.CharField(max_length=128)
    description = models.TextField()
    reporter = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    assignee = models.ForeignKey(
            get_user_model(),
            on_delete=models.CASCADE,
            related_name="assignee"
    )
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
```

### Note 2
```
class Status(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=128)
```