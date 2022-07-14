USER_NOT_FOUND = "Unable to locate user"
PARENT_NOT_FOUND = "Error finding parent group"
GROUP_DUPE = "A group with this name already exists under this parent"
GROUP_POST_ERROR = "Error creating group"
GROUP_POST_ADMIN_ERROR = "Group created, but an issue occurred creating group admin"
INVALID_SCOPE = "Scope must be equal to or a subset of the parent group's scope"

ADMIN_UNAUTHORIZED = "Unauthorized: Only Artemis Admins can set 'admin' to true"
ADMIN_INVALID = "Key 'admin' must be a boolean"
PARENT_ADMIN_COMBO_INVALID = "Unauthorized: Only Artemis Admins can create groups without a parent"
USER_NOT_GROUP_ADMIN = "Unauthorized: User must be group admin to perform this action"
FEATURE_INVALID = "Feature not authorized in parent group"
UNAUTHORIZED_SCOPE = "Scope not authorized in parent group"
GROUP_ID_NONE = "Group ID cannot be missing"
USER_KEY_NOT_GROUP_KEY = "API key does not have permissions for this group"
NO_PERMISSIONS = "User/Key does not have permissions for this group"
