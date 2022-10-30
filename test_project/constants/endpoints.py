class Endpoints:
    CREATE_USER = "/user/create"
    CREATE_POST = "/post"
    GET_INFO_POST_BY_ID = "/posts"
    SET_LIKE_ON_POST = "/like"
    VALIDATE_IK_ON_POST = "/likes"
    DELETE_POST = f"{CREATE_POST}/delete"
    REBLOG_POST = f"{CREATE_POST}/reblog"
    EDIT_TEXT = f"{CREATE_POST}/edit"
    FOLLOWING_USERS = "/following"

