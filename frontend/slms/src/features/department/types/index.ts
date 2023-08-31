export type Department = {
  name: string
  code: string
  description: string
}

export type DepartmentDetail = Department & {
  student_count: number
  course_count: number
}
