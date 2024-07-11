LEETCODE_GRAPH_API = "https://leetcode.com/graphql"
# limit doesn't work if given more than 20
LEETCODE_API_PAYLOAD = {"operationName":"getRecentSubmissionList","variables":{"username":"FaizAlam"},"query":"query getRecentSubmissionList($username: String!, $limit: Int) {\n  recentSubmissionList(username: $username, limit: $limit) {\n    title\n    titleSlug\n    timestamp\n    statusDisplay\n    lang\n    __typename\n  }\n  languageList {\n    id\n    name\n    verboseName\n    __typename\n  }\n}\n"}

LEETCODE_API_PAYLOAD_v2 = {"query":"\n    query recentAcSubmissions($username: String!, $limit: Int!) {\n  recentAcSubmissionList(username: $username, limit: $limit) {\n    id\n    title\n    titleSlug\n    timestamp\n  }\n}\n    ","variables":{"username":"faizalam","limit":40},"operationName":"recentAcSubmissions"}

# mailtrap credentials
MAIL_SMTP_SERVER = "live.smtp.mailtrap.io"
MAIL_SMTP_PORT = 587

MAIL_LOGIN="api"
MAIL_PASSWORD="86ff5df32b2c9c4b10a1ccb29f48227c"

LEETCODE_PROFILE_API = {"query":"\n    query userPublicProfile($username: String!) {\n  matchedUser(username: $username) {\n    contestBadge {\n      name\n      expired\n      hoverText\n      icon\n    }\n    username\n    githubUrl\n    twitterUrl\n    linkedinUrl\n    profile {\n      ranking\n      userAvatar\n      realName\n      aboutMe\n      school\n      websites\n      countryName\n      company\n      jobTitle\n      skillTags\n      postViewCount\n      postViewCountDiff\n      reputation\n      reputationDiff\n      solutionCount\n      solutionCountDiff\n      categoryDiscussCount\n      categoryDiscussCountDiff\n    }\n  }\n}\n    ","variables":{"username":"FaizAlam"},"operationName":"userPublicProfile"}


# this query gives all the submissions of the user but needs cookie to be passed in headers
# since we won't have cookie of other users, we won't be able to use this query
LEETCODE_PROGRESS_PAYLOAD = {"query":"\n    query progressList($pageNo: Int, $numPerPage: Int, $filters: ProgressListFilterInput) {\n  isProgressCalculated\n  solvedQuestionsInfo(pageNo: $pageNo, numPerPage: $numPerPage, filters: $filters) {\n    currentPage\n    pageNum\n    totalNum\n    data {\n      totalSolves\n      question {\n        questionFrontendId\n        questionTitle\n        questionDetailUrl\n        difficulty\n        topicTags {\n          name\n          slug\n        }\n      }\n      lastAcSession {\n        time\n        wrongAttempts\n      }\n    }\n  }\n}\n    ","variables":{"pageNo":1,"numPerPage":10,"filters":{"orderBy":"LAST_SOLVED","sortOrder":"DESCENDING"}},"operationName":"progressList"}

#user names to test
# u_noob_i
# faizalam
# ajinkya1p3