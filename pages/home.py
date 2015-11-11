# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from pages.base import Base
from pages.tasks.task_details import TaskDetailsPage
from pages.tasks.available_tasks import AvailableTasksPage


class HomePage(Base):

    _page_title = 'Mozilla One and Done'

    _displayed_profile_name_locator = (By.CSS_SELECTOR, '.billboard h3')
    _task_in_progress_locator = (By.ID, 'task-in-progress')
    _pick_a_task_locator = (By.ID, 'pick-a-task')

    @property
    def displayed_profile_name(self):
        return self.selenium.find_element(*self._displayed_profile_name_locator).text

    @property
    def is_task_in_progress(self):
        return self.is_element_visible(self._task_in_progress_locator)

    @property
    def task_in_progress(self):
        return self.selenium.find_element(*self._task_in_progress_locator).text

    def click_task_in_progress(self):
        self.selenium.find_element(*self._task_in_progress_locator).click()
        return TaskDetailsPage(self.base_url, self.selenium).wait_for_page_to_load()

    def click_pick_a_task_button(self):
        self.selenium.find_element(*self._pick_a_task_locator).click()
        return AvailableTasksPage(self.base_url, self.selenium).wait_for_page_to_load()
