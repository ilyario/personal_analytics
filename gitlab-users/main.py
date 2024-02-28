import gitlab
import pandas as pd
import streamlit as st
import os

GITLAB_URL = os.getenv("GITLAB_URL")
GITLAB_TOKEN = os.getenv("GITLAB_TOKEN")

gl = gitlab.Gitlab(url=GITLAB_URL, private_token=GITLAB_TOKEN)

project_ids = [1, 2, 3]

st.write("# Access to gitlab project")

access_dict = {
    gitlab.const.AccessLevel.OWNER: "MAINTAINER",
    gitlab.const.AccessLevel.MAINTAINER: "MAINTAINER",
    gitlab.const.AccessLevel.DEVELOPER: "DEVELOPER",
    gitlab.const.AccessLevel.REPORTER: "REPORTER",
}

project_dict = {"group1": ["project1", "project2"]}

access = []

for project_id in project_ids:
    project = gl.projects.get(project_id)
    members = project.members.list(get_all=True)
    for member in members:
        if "bot" not in member.username:
            access.append(
                {
                    "project": project.name,
                    "username": member.username,
                    "access_level": access_dict.get(member.access_level),
                }
            )

df = pd.DataFrame(data=access)

df["group"] = df["project"].map(
    {project: key for key, projects in project_dict.items() for project in projects}
)

st.write(f"### ALL ACCESS")
df_sorted = df.sort_values(by=["project", "access_level", "username"])
st.write(df_sorted)

grouped_df_project = (
    df_sorted.groupby(["group", "project", "access_level"])["username"]
    .agg(list)
    .reset_index()
)

grouped_by_access_level = grouped_df_project.groupby("access_level")

st.write(f"### ALL ACCESS by project")
st.write(grouped_df_project)

for access_level, group in grouped_by_access_level:
    st.write(f"### Access Level: {access_level}")
    st.write(group)
