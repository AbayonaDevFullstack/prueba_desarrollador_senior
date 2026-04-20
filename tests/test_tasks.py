"""
Technical test — Task Manager API
Run with: pytest tests/ -v
All tests must pass to complete the challenge.
"""


def test_create_task_returns_201(client):
    """POST /tasks must respond with HTTP 201 Created."""
    response = client.post("/tasks/", json={"title": "New task"})
    assert response.status_code == 201, (
        f"Expected 201 Created but got {response.status_code}. "
        "Review the POST /tasks endpoint."
    )
    data = response.json()
    assert data["title"] == "New task"


def test_patch_actually_updates_task(client):
    """PATCH /tasks/{id} must persist and return the updated values."""
    created = client.post("/tasks/", json={"title": "Original title", "status": "pending"})
    task_id = created.json()["id"]

    response = client.patch(f"/tasks/{task_id}", json={"title": "Updated title", "status": "in_progress"})
    assert response.status_code == 200
    data = response.json()

    assert data["title"] == "Updated title", (
        f"Expected title 'Updated title' but got '{data['title']}'. "
        "The PATCH endpoint is not persisting changes."
    )
    assert data["status"] == "in_progress", (
        f"Expected status 'in_progress' but got '{data['status']}'. "
        "The PATCH endpoint is not persisting changes."
    )


def test_filter_by_status_returns_correct_tasks(client):
    """GET /tasks?status=done must return only tasks with status 'done'."""
    client.post("/tasks/", json={"title": "Task A", "status": "pending"})
    client.post("/tasks/", json={"title": "Task B", "status": "done"})
    client.post("/tasks/", json={"title": "Task C", "status": "done"})

    response = client.get("/tasks/?status=done")
    assert response.status_code == 200
    tasks = response.json()

    assert len(tasks) == 2, (
        f"Expected 2 tasks with status 'done' but got {len(tasks)}. "
        "Review the status filter logic."
    )
    statuses = {t["status"] for t in tasks}
    assert statuses == {"done"}, (
        f"Expected only 'done' tasks but got statuses: {statuses}. "
        "The filter is returning incorrect results."
    )
