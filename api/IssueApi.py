import json
from flask import Blueprint, request, jsonify
from database.DatabaseManager import get_single_row, get_multiple_rows, create_single_row, delete_or_update_row, _Action

issues_api = Blueprint('issues_api', __name__)


@issues_api.route('/issues', methods=['POST'])
def create_issue():
    try:
        issue_data = request.get_json()
        result = create_single_row('Issues', issue_data)

        if result:
            return jsonify({'message': 'Issue created successfully'}), 200
        else:
            return jsonify({'message': 'Failed to create issue'}), 500
    except Exception as e:
        return jsonify({'message': 'Error creating issue', 'error': str(e)}), 500


@issues_api.route('/issues/<int:issue_id>', methods=['GET'])
def get_issue(issue_id):
    issue = get_single_row('Issues', issue_id)
    if issue:
        issue_json_str = issue[0]
        issue_dict = json.loads(issue_json_str)
        return jsonify(issue_dict), 200
    else:
        return jsonify({'message': 'Issue not found'}), 404


@issues_api.route('/issues', methods=['GET'])
def get_issues():
    issues = get_multiple_rows('Issues', 'IssueID')
    if issues:
        return jsonify({'issues': issues}), 200
    else:
        return jsonify({'message': 'No issues found'}), 404


@issues_api.route('/issues/<int:issue_id>', methods=['PUT'])
def update_issue(issue_id):
    try:
        issue_data = request.get_json()
        result = delete_or_update_row('Issues', issue_id, 'IssueID', _Action.UPDATE, issue_data)

        return jsonify({'issue_id': issue_id, 'success': result, 'message': 'Issue updated successfully' if result else 'Failed to update issue'}), 200
    except Exception as e:
        return jsonify({'message': 'Error updating issue', 'error': str(e)}), 500


@issues_api.route('/issues/<int:issue_id>', methods=['DELETE'])
def delete_issue(issue_id):
    result = delete_or_update_row('Issues', issue_id, 'IssueID', _Action.DELETE)

    if result:
        return jsonify({'message': f'Issue with id = {issue_id} deleted successfully'}), 200
    else:
        return jsonify({'message': 'Failed to delete issue'}), 500
