function toggleFields() {
    const role = document.getElementById('join_as').value;
    document.getElementById('mentor_fields').style.display = role === 'Mentor' ? 'block' : 'none';
    document.getElementById('learner_fields').style.display = role === 'Learner' ? 'block' : 'none';
}
