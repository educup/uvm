from typing import List, Optional


class Version:
    def __init__(self, major: int, minor: int, patch: int, build: int, code: int):
        self.major = major
        self.minor = minor
        self.patch = patch
        self.build = build
        self.code = code

    def __str__(self) -> str:
        return f"{self.major}.{self.minor}.{self.patch}b{self.build}({self.code})"

    def set_major(self, number: int):
        self.major = number

    def set_minor(self, number: int):
        self.minor = number

    def set_patch(self, number: int):
        self.patch = number

    def set_build(self, number: int):
        self.build = number

    def set_code(self, number: int):
        self.code = number

    def set_major_up(self):
        self.set_major(self.major + 1)
        self.set_minor(0)
        self.set_patch(0)
        self.set_build(0)
        self.set_code_up()

    def set_minor_up(self):
        self.set_minor(self.minor + 1)
        self.set_patch(0)
        self.set_build(0)
        self.set_code_up()

    def set_patch_up(self):
        self.set_patch(self.patch + 1)
        self.set_build(0)
        self.set_code_up()

    def set_build_up(self):
        self.set_build(self.build + 1)
        self.set_code_up()

    def set_code_up(self):
        self.code += 1

    @staticmethod
    def get(filename: str):
        major = -1
        minor = -1
        patch = -1
        build = -1
        code = -1
        with open(filename, mode="r") as file:
            mark = False
            for line in file.readlines():
                if "bundleVersion: " in line:
                    content = line.split(": ")[1]
                    content_splited = content.split(".")
                    if len(content_splited) != 3:
                        raise Exception(
                            "Version should be x.y.z format and "
                            + "x, y and z should be an integers"
                        )
                    major_str, minor_str, patch_str = content_splited
                    try:
                        major = int(major_str)
                        minor = int(minor_str)
                        patch = int(patch_str)
                    except ValueError:
                        raise Exception(
                            "Version should be x.y.z format and "
                            + "x, y and z should be an integers"
                        )
                elif "iPhone: " in line and mark:
                    content = line.split(": ")[1]
                    try:
                        build = int(content)
                    except ValueError:
                        raise Exception("Build should be an integer")
                    mark = False
                elif "AndroidBundleVersionCode: " in line:
                    content = line.split(": ")[1]
                    try:
                        code = int(content)
                    except ValueError:
                        raise Exception("Code should be an integer")
                mark = mark or "buildNumber:" in line
                if (
                    major != -1
                    and minor != -1
                    and patch != -1
                    and build != -1
                    and code != -1
                ):
                    break
        version = Version(major, minor, patch, build, code)
        if major == -1 or minor == -1 or patch == -1 or build == -1 or code == -1:
            raise Exception(f"Error parsing file: {version}")
        return version

    def set(self, filename: str):
        lines: List[str] = []
        with open(filename, mode="r") as file:
            mark = False
            for line in file.readlines():
                if "bundleVersion: " in line:
                    content = line.split(":")[0]
                    lines.append(f"{content}: {self.major}.{self.minor}.{self.patch}\n")
                elif "iPhone: " in line and mark:
                    content = line.split(":")[0]
                    lines.append(f"{content}: {self.build}\n")
                    mark = False
                elif "AndroidBundleVersionCode: " in line:
                    content = line.split(":")[0]
                    lines.append(f"{content}: {self.code}\n")
                else:
                    lines.append(line)
                mark = mark or "buildNumber:" in line
        with open(filename, mode="w") as file:
            file.writelines(lines)

    @staticmethod
    def parse(version: str) -> Optional["Version"]:
        if not version.endswith(")"):
            return None
        try:
            major = int(version.split(".")[0])
            minor = int(version.split(".")[1])
            patch = int(version.split(".")[2].split("b")[0])
            build = int(version.split("b")[1].split("(")[0])
            code = int(version.split("(")[1].strip(")"))
            return Version(major, minor, patch, build, code)
        except Exception:
            return None
